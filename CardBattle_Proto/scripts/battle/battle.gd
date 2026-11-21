class_name Battle
extends RefCounted
## 戦闘の計算だけを受け持つ。画面には触らない。
## 起きたことは events に積み、画面側が take_events() で受け取って演出する。
## 調整する数値は data/params.json に【日本語名】で置いてある（桜井 #046 / #068）。
##
## 芯（桜井 #006 リスクとリターン）：
##   興奮が高いほど攻撃が強くなる（高揚）。ただし100を超えると絶頂して精を失う。
##   限界ぎりぎりで戦うほど強いが、一歩間違えると果てる。

const LEWD_CARDS := ["charm", "fluster"]

const STATUS_NAMES := {
	"sensitive": "敏感", "bound": "拘束", "afterglow": "脱力",
	"iron": "鋼の意志", "focus": "集中", "weak": "白け", "shaken": "動揺",
}
const STATUS_HELP := {
	"sensitive": "受ける興奮が増える",
	"bound": "次のターン、引く枚数が1減る",
	"afterglow": "次のターン、気力が1減る",
	"iron": "毎ターン、この数だけ忍耐を得る",
	"focus": "次の攻撃の削りがこの数だけ増える",
	"weak": "相手の誘惑が弱まる",
	"shaken": "相手が受ける削りが増える",
}

## data/params.json が読めないときの値
const DEFAULT_PARAMS := {
	"【ターンごとの気力】": 3,
	"【ターンごとに引く枚数】": 5,
	"【手札の上限】": 10,
	"【精の数】": 3,
	"【絶頂する興奮】": 100,
	"【絶頂のあとの興奮】": 40,
	"【絶頂で付く敏感】": 1,
	"【敏感1つあたりの興奮の増加率】": 0.25,
	"【白けのときの誘惑の倍率】": 0.6,
	"【動揺のときの削りの倍率】": 1.5,
	"【高揚が上がる興奮】": [40, 70],
	"【高揚の段階の名前】": ["平常", "火照り", "限界寸前"],
	"【高揚の削りの倍率】": [1.0, 1.3, 1.7],
}

var P: Dictionary = DEFAULT_PARAMS.duplicate()
var rng := RandomNumberGenerator.new()
var cards_db: Dictionary = {}
var enemy: Dictionary = {}
var mult := 1.0

# 主人公
var max_energy := 3
var energy := 0
var max_stocks := 3
var stocks := 3
var arousal := 0
var block := 0
var p_status: Dictionary = {}
var draw_pile: Array = []
var hand: Array = []
var discard_pile: Array = []
var exhaust_pile: Array = []

# 相手
var e_hp := 0
var e_max := 0
var e_status: Dictionary = {}
var pattern_pos := 0
var intent_id := ""
var phase := 1

var turn := 0
var result := ""  # "" / "win" / "lose"
var climaxes := 0
var surrendered := false
var best_tier := 0  # この戦闘でいちばん高かった高揚の段階（褒める演出に使う）

var _uid := 0
var _focus_bonus := 0
var events: Array = []


func setup(p_cards_db: Dictionary, p_enemy: Dictionary, deck: Array, p_mult: float = 1.0, seed_value: int = -1, params: Dictionary = {}) -> void:
	for k in params:
		P[k] = params[k]
	cards_db = p_cards_db
	enemy = p_enemy
	mult = p_mult
	max_energy = int(P["【ターンごとの気力】"])
	max_stocks = int(P["【精の数】"])
	stocks = max_stocks
	if seed_value >= 0:
		rng.seed = seed_value
	else:
		rng.randomize()
	for id in deck:
		draw_pile.append(_make(str(id)))
	_shuffle(draw_pile)
	e_max = int(enemy.get("hp", 40))
	e_hp = e_max
	_pick_intent()
	start_player_turn()


# ---------------------------------------------------------------- 便利関数

func climax_at() -> int:
	return int(P["【絶頂する興奮】"])


func hand_max() -> int:
	return int(P["【手札の上限】"])


func _make(id: String) -> Dictionary:
	_uid += 1
	return {"uid": _uid, "id": id}


func card_def(c: Dictionary) -> Dictionary:
	return cards_db.get(c["id"], {})


func _shuffle(arr: Array) -> void:
	for i in range(arr.size() - 1, 0, -1):
		var j := rng.randi_range(0, i)
		var t = arr[i]
		arr[i] = arr[j]
		arr[j] = t


func _ev(type: String, data: Dictionary = {}) -> void:
	data["type"] = type
	events.append(data)


func take_events() -> Array:
	var out := events
	events = []
	return out


func _decay(dict: Dictionary, keys: Array) -> void:
	for k in keys:
		if dict.has(k):
			dict[k] = int(dict[k]) - 1
			if dict[k] <= 0:
				dict.erase(k)


func status_text(dict: Dictionary) -> String:
	var parts := PackedStringArray()
	for k in dict:
		parts.append("%s%d" % [STATUS_NAMES.get(k, k), int(dict[k])])
	return "　".join(parts)


# ---------------------------------------------------------------- 高揚（芯の仕組み）

## 今の高揚の段階（0=平常, 1=火照り, 2=限界寸前）
func tier() -> int:
	return tier_of(arousal)


func tier_of(a: int) -> int:
	var t := 0
	for th in P["【高揚が上がる興奮】"]:
		if a >= int(th):
			t += 1
	return t


func tier_name(t: int = -1) -> String:
	return P["【高揚の段階の名前】"][tier() if t < 0 else t]


func tier_mult(t: int = -1) -> float:
	return float(P["【高揚の削りの倍率】"][tier() if t < 0 else t])


## 攻撃の削り量（高揚と動揺を反映）。画面のカード表示にも使う。
func damage_value(base: int, with_focus: int = 0) -> int:
	var d := float(base + with_focus) * tier_mult()
	if int(e_status.get("shaken", 0)) > 0:
		d *= float(P["【動揺のときの削りの倍率】"])
	return int(round(d))


# ---------------------------------------------------------------- ターンの流れ

func start_player_turn() -> void:
	turn += 1
	block = 0
	energy = max_energy
	if int(p_status.get("afterglow", 0)) > 0:
		energy -= 1
		_ev("log", {"text": "脱力して、気力が1減った"})
	if int(p_status.get("iron", 0)) > 0:
		block += int(p_status["iron"])
		_ev("block", {"val": int(p_status["iron"])})
	var n := int(P["【ターンごとに引く枚数】"])
	if int(p_status.get("bound", 0)) > 0:
		n -= 1
		_ev("log", {"text": "巻きつかれて、引く枚数が1減った"})
	_decay(p_status, ["afterglow", "bound"])
	_ev("turn_start", {"turn": turn})
	draw(n)


func draw(n: int) -> void:
	for i in n:
		if result != "":
			return
		if draw_pile.is_empty():
			if discard_pile.is_empty():
				return
			draw_pile = discard_pile
			discard_pile = []
			_shuffle(draw_pile)
			_ev("reshuffle")
		var c: Dictionary = draw_pile.pop_back()
		if hand.size() >= hand_max():
			discard_pile.append(c)
			continue
		hand.append(c)
		_ev("draw", {"uid": c["uid"]})
		var d := card_def(c)
		for eff in d.get("on_draw", []):
			_apply_player_effect(eff, d)


func can_play(idx: int) -> bool:
	if result != "" or idx < 0 or idx >= hand.size():
		return false
	var d := card_def(hand[idx])
	if d.get("unplayable", false):
		return false
	return int(d.get("cost", 0)) <= energy


## 使えない理由（画面で伝えるため）。使えるなら空文字。
func why_unplayable(idx: int) -> String:
	if idx < 0 or idx >= hand.size():
		return ""
	var d := card_def(hand[idx])
	if d.get("unplayable", false):
		return "「%s」は使えないカード。目を逸らすなどで除外できる" % d.get("name", "")
	if int(d.get("cost", 0)) > energy:
		return "気力が足りない（あと%d要る）" % (int(d.get("cost", 0)) - energy)
	return ""


func play(idx: int) -> bool:
	if not can_play(idx):
		return false
	var c: Dictionary = hand[idx]
	var d := card_def(c)
	energy -= int(d.get("cost", 0))
	hand.remove_at(idx)
	_ev("play", {"uid": c["uid"], "name": d.get("name", "")})
	_focus_bonus = 0
	if d.get("type", "") == "attack" and p_status.has("focus"):
		_focus_bonus = int(p_status["focus"])
		p_status.erase("focus")
	for eff in d.get("effects", []):
		_apply_player_effect(eff, d)
		if result != "":
			break
	_focus_bonus = 0
	if d.get("exhaust", false) or d.get("type", "") == "power":
		exhaust_pile.append(c)
	else:
		discard_pile.append(c)
	return true


func end_turn() -> void:
	if result != "":
		return
	for c in hand.duplicate():
		var d := card_def(c)
		for eff in d.get("end_in_hand", []):
			_apply_player_effect(eff, d)
			if result != "":
				return
	for c in hand:
		if card_def(c).get("ethereal", false):
			exhaust_pile.append(c)
		else:
			discard_pile.append(c)
	hand.clear()
	_ev("turn_end")
	_enemy_turn()
	if result != "":
		return
	_decay(e_status, ["weak", "shaken"])
	_decay(p_status, ["sensitive"])
	_pick_intent()
	start_player_turn()


## おねだり：自分から負けを選ぶ。
func surrender() -> void:
	if result != "":
		return
	surrendered = true
	result = "lose"
	_ev("surrender")
	_ev("lose")


# ---------------------------------------------------------------- 効果

func _apply_player_effect(eff: Dictionary, _d: Dictionary) -> void:
	var op: String = eff.get("op", "")
	var val := int(eff.get("val", 0))
	match op:
		"damage":
			for h in int(eff.get("hits", 1)):
				var dmg := damage_value(val, _focus_bonus)
				_focus_bonus = 0
				e_hp = maxi(0, e_hp - dmg)
				_ev("enemy_damage", {"val": dmg, "tier": tier()})
				if e_hp <= 0:
					_win()
					return
		"block":
			block += val
			_ev("block", {"val": val})
		"calm":
			var before := arousal
			arousal = maxi(0, arousal - val)
			_ev("calm", {"val": before - arousal})
			_check_tier_change(before)
		"draw":
			draw(val)
		"energy":
			energy = maxi(0, energy + val)
			_ev("energy", {"val": val})
		"arousal":
			_gain_arousal(val, false)
		"cleanse":
			var removed := 0
			for i in range(hand.size() - 1, -1, -1):
				if hand[i]["id"] in LEWD_CARDS:
					exhaust_pile.append(hand[i])
					hand.remove_at(i)
					removed += 1
			if removed > 0:
				_ev("log", {"text": "誘惑のカードを%d枚振り払った" % removed})
		"status":
			var id: String = eff["id"]
			p_status[id] = int(p_status.get(id, 0)) + int(eff.get("n", 1))
			_ev("status", {"who": "player", "id": id})
		"clear_status":
			p_status.erase(eff["id"])
		"enemy_status":
			var id: String = eff["id"]
			e_status[id] = int(e_status.get(id, 0)) + int(eff.get("n", 1))
			_ev("status", {"who": "enemy", "id": id})


## 相手から受ける興奮の見込み（敏感・白け・責めの強さを反映）
func preview_arousal(val: int) -> int:
	var v := float(val) * mult
	v *= 1.0 + float(P["【敏感1つあたりの興奮の増加率】"]) * int(p_status.get("sensitive", 0))
	if int(e_status.get("weak", 0)) > 0:
		v *= float(P["【白けのときの誘惑の倍率】"])
	return int(round(v))


## 相手の次の行動で、忍耐を引いたあとに実際に入る興奮の見込み
func incoming_arousal() -> int:
	var total := 0
	for eff in current_move().get("effects", []):
		if eff.get("op", "") == "arouse":
			total += preview_arousal(int(eff["val"])) * int(eff.get("hits", 1))
	return maxi(0, total - block)


func _gain_arousal(val: int, from_enemy: bool) -> void:
	var amount := preview_arousal(val) if from_enemy else val
	if from_enemy and block > 0:
		var absorbed := mini(block, amount)
		block -= absorbed
		amount -= absorbed
		if absorbed > 0:
			_ev("blocked", {"val": absorbed})
	if amount <= 0:
		return
	var before := arousal
	arousal += amount
	_ev("arousal", {"val": amount, "from_enemy": from_enemy})
	if arousal < climax_at():
		best_tier = maxi(best_tier, tier())
	if arousal >= climax_at():
		while arousal >= climax_at() and result == "":
			_climax()
	else:
		_check_tier_change(before)


func _check_tier_change(before: int) -> void:
	var t0 := tier_of(before)
	var t1 := tier()
	if t1 != t0:
		best_tier = maxi(best_tier, t1)
		_ev("tier", {"tier": t1, "up": t1 > t0})


func _climax() -> void:
	climaxes += 1
	best_tier = maxi(best_tier, tier())
	stocks -= 1
	arousal = int(P["【絶頂のあとの興奮】"])
	p_status["afterglow"] = 1
	# イったばかりで感じやすくなる
	var s := int(P["【絶頂で付く敏感】"])
	if s > 0:
		p_status["sensitive"] = int(p_status.get("sensitive", 0)) + s
	var heal := int(enemy.get("drain_heal", 5))
	e_hp = mini(e_max, e_hp + heal)
	_ev("climax", {"stocks": stocks, "heal": heal})
	if stocks <= 0:
		result = "lose"
		_ev("lose")


func _win() -> void:
	best_tier = maxi(best_tier, tier())
	result = "win"
	_ev("win", {"climaxes": climaxes, "turns": turn, "best_tier": best_tier})


# ---------------------------------------------------------------- 相手の行動

func _pattern() -> Array:
	if phase == 1 and enemy.has("pattern2") and e_hp * 2 <= e_max:
		phase = 2
		pattern_pos = 0
		_ev("phase2")
	return enemy.get("pattern2" if phase == 2 else "pattern", [])


func _pick_intent() -> void:
	var p := _pattern()
	if p.is_empty():
		intent_id = ""
		return
	intent_id = str(p[pattern_pos % p.size()])
	pattern_pos += 1


func current_move() -> Dictionary:
	return enemy.get("moves", {}).get(intent_id, {})


func intent_text() -> String:
	var mv := current_move()
	var parts := PackedStringArray()
	for eff in mv.get("effects", []):
		match eff.get("op", ""):
			"arouse":
				var hits := int(eff.get("hits", 1))
				var s := "興奮+%d" % preview_arousal(int(eff["val"]))
				if hits > 1:
					s += "×%d" % hits
				parts.append(s)
			"add_card":
				var cname: String = cards_db.get(eff["card"], {}).get("name", eff["card"])
				var where: String = {"draw": "山札", "discard": "捨て札", "hand": "手札"}.get(eff.get("to", "discard"), "")
				parts.append("%s×%dを%sへ" % [cname, int(eff.get("n", 1)), where])
			"status":
				parts.append("%s%d" % [STATUS_NAMES.get(eff["id"], eff["id"]), int(eff.get("n", 1))])
			"heal":
				parts.append("余裕+%d" % int(eff["val"]))
	if mv.has("telegraph"):
		parts.append(mv["telegraph"])
	return "、".join(parts)


func _enemy_turn() -> void:
	var mv := current_move()
	_ev("enemy_move", {"name": mv.get("name", ""), "id": intent_id})
	for eff in mv.get("effects", []):
		var op: String = eff.get("op", "")
		match op:
			"arouse":
				for h in int(eff.get("hits", 1)):
					_gain_arousal(int(eff["val"]), true)
					if result != "":
						return
			"add_card":
				var n := int(eff.get("n", 1))
				for i in n:
					var c := _make(str(eff["card"]))
					var to: String = eff.get("to", "discard")
					if to == "draw":
						draw_pile.insert(rng.randi_range(0, draw_pile.size()), c)
					elif to == "hand" and hand.size() < hand_max():
						hand.append(c)
					else:
						discard_pile.append(c)
				_ev("add_card", {"card": eff["card"], "n": n, "to": eff.get("to", "discard")})
			"status":
				var id: String = eff["id"]
				p_status[id] = int(p_status.get(id, 0)) + int(eff.get("n", 1))
				_ev("status", {"who": "player", "id": id})
			"heal":
				var before := e_hp
				e_hp = mini(e_max, e_hp + int(eff["val"]))
				_ev("enemy_heal", {"val": e_hp - before})
