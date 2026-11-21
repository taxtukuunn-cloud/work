class_name Bot
extends RefCounted
## 自動で遊ぶ係。勝率の確認と、壊れていないかの確認に使う。
## 桜井 #219：完璧な守りではなく、高揚を使って攻める打ち方をさせる。

## 打ち方："smart"＝考えて打つ／"attack"＝守らず攻撃だけ／"defend"＝守り優先
static var mode := "smart"


## 1ターン分を遊ぶ（使えるカードを点数の高い順に使い、最後にターン終了）
static func play_turn(b: Battle) -> void:
	for _i in 20:
		var best := -1
		var best_score := 0.0
		for i in b.hand.size():
			if not b.can_play(i):
				continue
			var s := score(b, b.card_def(b.hand[i]))
			if s > best_score:
				best_score = s
				best = i
		if best < 0:
			break
		b.play(best)
		if b.result != "":
			return
	b.end_turn()


static func score(b: Battle, d: Dictionary) -> float:
	var ops := []
	for eff in d.get("effects", []):
		ops.append(eff.get("op", ""))
	if mode == "attack":
		if "damage" in ops:
			return 10.0
		if "block" in ops or "calm" in ops:
			return -1.0
	var need := b.incoming_arousal()
	var limit := b.climax_at()
	var danger := b.arousal + need >= limit
	var s := 0.0
	var self_arousal := 0
	var calm := 0
	for eff in d.get("effects", []):
		var val := int(eff.get("val", 0))
		match eff.get("op", ""):
			"damage":
				var total := b.damage_value(val) * int(eff.get("hits", 1))
				s += 6.0 + total * 0.8
				if total >= b.e_hp:
					s += 50.0
			"block":
				# 来る興奮より多い忍耐は無駄
				s += (8.0 + min(val, need) * 0.8) if need > 0 else 0.0
				if danger and need > 0:
					s += 12.0
			"calm":
				calm += val
			"draw":
				s += 7.0 * val
			"energy":
				s += 5.0 * val
			"arousal":
				self_arousal += val
			"cleanse":
				var lewd := 0
				for c in b.hand:
					if c["id"] in Battle.LEWD_CARDS:
						lewd += 1
				s += 8.0 * lewd + 0.5
			"status":
				s += 9.0
			"clear_status":
				s += 6.0 if b.p_status.has("sensitive") else 0.0
			"enemy_status":
				s += 7.0
	if calm > 0:
		if danger:
			s += 14.0 + calm * 0.4
		elif b.arousal + need >= limit - 15:
			s += 4.0 + calm * 0.3
		else:
			# 危なくないなら高揚を下げるのはもったいない
			s += 0.2
	if self_arousal > 0:
		var after := b.arousal + self_arousal
		if after + need >= limit - 8:
			return -1.0
		# 高揚の段階が上がるなら得
		s += 6.0 * (b.tier_of(after) - b.tier())
		s -= self_arousal * 0.15
	if mode == "defend" and ("block" in ops or "calm" in ops):
		s = s * 3.0 + 20.0
	return s / max(1.0, float(d.get("cost", 0)) + 0.5)


## 1戦を最後まで遊ばせて結果を返す
static func run_battle(cards: Dictionary, enemy: Dictionary, deck: Array, mult: float, seed_value: int) -> Dictionary:
	var b := Battle.new()
	b.setup(cards, enemy, deck, mult, seed_value, DB.params)
	var guard := 0
	while b.result == "" and guard < 60:
		play_turn(b)
		b.take_events()
		guard += 1
	return {"result": b.result if b.result != "" else "timeout", "turns": b.turn, "climaxes": b.climaxes, "hp_left": b.e_hp, "best_tier": b.best_tier}
