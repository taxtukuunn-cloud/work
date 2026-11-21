extends Node
## 画面なしで動かすテスト。
##   godot --headless --path . res://tests/test_runner.tscn -- --no-save [--sim]
## 失敗があれば終了コード 1 で終わる。

var failures := 0


func _ready() -> void:
	_test_scripts()
	_test_data()
	_test_basic_rules()
	_test_climax_and_lose()
	_test_surrender()
	_test_preview_matches()
	_test_cards_all_playable()
	if "--sim" in OS.get_cmdline_user_args():
		_simulate()
	if "--policy" in OS.get_cmdline_user_args():
		_policy_check()
	if "--cardsim" in OS.get_cmdline_user_args():
		_card_sim()
	print("")
	print("失敗: %d" % failures)
	get_tree().quit(1 if failures > 0 else 0)


func check(cond: bool, msg: String) -> void:
	if cond:
		print("  OK  ", msg)
	else:
		failures += 1
		print("  NG  ", msg)


## すべてのスクリプトが読み込めるか（構文の誤りでテストが黙って通らないように）
func _test_scripts() -> void:
	print("[スクリプト]")
	for dir in ["res://scripts", "res://scripts/autoload", "res://scripts/battle", "res://scripts/ui", "res://tests", "res://tools"]:
		for f in DirAccess.get_files_at(dir):
			if not f.ends_with(".gd"):
				continue
			var path: String = dir + "/" + f
			var sc = load(path)
			check(sc != null and (sc as GDScript).can_instantiate(), "%s が読み込める" % path)


func _test_data() -> void:
	print("[データ]")
	check(DB.cards.size() >= 20, "カードが20種以上ある (%d)" % DB.cards.size())
	check(DB.enemies.size() == 3, "敵が3体いる")
	for id in DB.starter_deck:
		check(DB.cards.has(id), "最初のデッキのカード %s がある" % id)
	for e in DB.enemies:
		for key in ["_intro", "_win", "_lose1", "_lose2"]:
			check(DB.scenes.has(e["id"] + key), "シーン %s%s がある" % [e["id"], key])
		for mid in e["pattern"] + e.get("pattern2", []):
			check(e["moves"].has(mid), "%s の行動 %s が定義されている" % [e["id"], mid])
		for mid in e["moves"]:
			for eff in e["moves"][mid]["effects"]:
				if eff["op"] == "add_card":
					check(DB.cards.has(eff["card"]), "%s が入れるカード %s がある" % [e["id"], eff["card"]])
	for sid in DB.scenes:
		var s: Dictionary = DB.scenes[sid]
		check(s["lines"].size() > 0, "シーン %s に本文がある" % sid)
		if s.get("enemy", "") != "":
			check(not DB.enemy(s["enemy"]).is_empty(), "シーン %s の相手 %s がいる" % [sid, s["enemy"]])


func _new_battle(deck: Array = DB.starter_deck, enemy_idx: int = 0, seed_value: int = 1) -> Battle:
	var b := Battle.new()
	b.setup(DB.cards, DB.enemies[enemy_idx], deck, 1.0, seed_value, DB.params)
	return b


func _test_basic_rules() -> void:
	print("[基本の決まり]")
	var b := _new_battle()
	check(b.hand.size() == 5, "最初に5枚引く")
	check(b.energy == 3, "気力は3")
	check(b.intent_id != "", "相手の次の行動が決まっている")
	# 斬撃を探して使う
	var idx := -1
	for i in b.hand.size():
		if b.hand[i]["id"] == "strike":
			idx = i
	if idx >= 0:
		var hp := b.e_hp
		b.play(idx)
		check(b.e_hp == hp - 6, "斬撃で余裕が6減る")
		check(b.energy == 2, "気力が1減る")
	var total := b.draw_pile.size() + b.hand.size() + b.discard_pile.size() + b.exhaust_pile.size()
	check(total == DB.starter_deck.size(), "カードの枚数が合っている")
	b.end_turn()
	check(b.turn == 2, "ターン終了で次のターンへ進む")
	check(b.hand.size() >= 5, "次のターンも5枚以上持っている")
	# 忍耐が興奮を防ぐ
	var b2 := _new_battle()
	b2.block = 100
	b2.end_turn()
	check(b2.arousal == 0 or b2.arousal < 10, "忍耐があれば興奮をほぼ防げる（%d）" % b2.arousal)


func _test_climax_and_lose() -> void:
	print("[絶頂と敗北]")
	var b := _new_battle()
	b.arousal = 99
	var hp := b.e_hp
	b._gain_arousal(5, false)
	check(b.stocks == 2, "100に届くと精が1減る")
	check(b.arousal == int(DB.params["【絶頂のあとの興奮】"]), "絶頂のあと興奮が戻る")
	check(b.e_hp == mini(b.e_max, hp + int(DB.enemies[0]["drain_heal"])), "相手が吸精で余裕を回復する")
	b.arousal = 99
	b._gain_arousal(5, false)
	b.arousal = 99
	b._gain_arousal(5, false)
	check(b.result == "lose", "精がなくなると敗北")


## 予告した興奮と、実際に入る興奮が一致するか（レビューの不具合1）
func _test_preview_matches() -> void:
	print("[予告と実際]")
	for ei in DB.enemies.size():
		var e: Dictionary = DB.enemies[ei]
		for mid in e["moves"]:
			var b := _new_battle(DB.starter_deck, ei, 5)
			b.intent_id = mid
			b.hand.clear()
			b.block = 0
			b.arousal = 0
			var expect := b.incoming_arousal()
			b._enemy_turn()
			check(b.arousal == expect or b.climaxes > 0, "%s「%s」：予告 %d ＝ 実際 %d" % [e["name"], e["moves"][mid]["name"], expect, b.arousal])


func _test_surrender() -> void:
	print("[おねだり]")
	var b := _new_battle()
	check(not b.can_surrender(), "最初はおねだりできない（追い詰められてから）")
	b.arousal = 45
	check(b.can_surrender(), "火照りになればおねだりできる")
	b.surrender()
	check(b.result == "lose" and b.surrendered, "おねだりで、すぐ敗北になる")


func _test_cards_all_playable() -> void:
	print("[全カード]")
	for id in DB.cards:
		var d: Dictionary = DB.cards[id]
		if d.get("unplayable", false):
			continue
		var b := _new_battle([id, "strike", "strike", "strike", "strike", "endure"], 2, 3)
		b.energy = 10
		var idx := -1
		for i in b.hand.size():
			if b.hand[i]["id"] == id:
				idx = i
		if idx < 0:
			b.hand.append(b._make(id))
			idx = b.hand.size() - 1
		var ok := b.play(idx)
		check(ok, "%s（%s）が使える" % [d["name"], id])


## 報酬カードを1枚足したときの勝率の変化（取ると損なカードがないかの確認）
func _card_sim() -> void:
	print("")
	print("[カード1枚ごとの勝率の変化（ヴェルザ・ふつう、最初のデッキ+強撃+そのカード）]")
	var n := 400
	var e: Dictionary = DB.enemies[2]
	var base_deck: Array = DB.starter_deck + ["heavy"]
	var base := _winrate(e, base_deck, n)
	print("  基準 %3d%%" % int(base * 100))
	var rows := []
	for id in DB.reward_pool():
		var w := _winrate(e, base_deck + [id], n)
		rows.append([w, id])
	rows.sort_custom(func(a, b): return a[0] > b[0])
	for r in rows:
		print("  %-8s %3d%%  (%+d)" % [DB.cards[r[1]]["name"], int(r[0] * 100), int((r[0] - base) * 100)])


func _winrate(e: Dictionary, deck: Array, n: int) -> float:
	var wins := 0
	for s in n:
		if Bot.run_battle(DB.cards, e, deck, 1.0, s * 7919 + 13)["result"] == "win":
			wins += 1
	return float(wins) / n


## 打ち方ごとの勝率（考えて打つ方が、攻撃連打より勝つこと。桜井 #006）
func _policy_check() -> void:
	print("")
	print("[打ち方ごとの勝率（ふつう、最初のデッキ+強撃）]")
	var deck: Array = DB.starter_deck + ["heavy"]
	var n := 300
	# 目標：考えて打つ勝率の範囲と、絶頂回数の範囲（レビューで決めた値）
	var goals := {"milda": [0.93, 1.0], "serpena": [0.82, 0.95], "verza": [0.6, 0.8]}
	for e in DB.enemies:
		var row := {}
		for m in ["smart", "attack", "defend"]:
			Bot.mode = m
			var wins := 0
			var turns := 0
			var climax := 0
			for s in n:
				var r := Bot.run_battle(DB.cards, e, deck, 1.0, s * 7919 + 13)
				if r["result"] == "win":
					wins += 1
				turns += int(r["turns"])
				climax += int(r["climaxes"])
			row[m] = [float(wins) / n, float(turns) / n, float(climax) / n]
		Bot.mode = "smart"
		print("  %s : 考えて %3d%%（%.1fターン・絶頂%.2f）／攻撃だけ %3d%%／守り優先 %3d%%" % [
			e["name"], int(row["smart"][0] * 100), row["smart"][1], row["smart"][2],
			int(row["attack"][0] * 100), int(row["defend"][0] * 100)])
		check(row["smart"][0] - row["attack"][0] >= 0.1 or row["smart"][0] >= 0.97, "%s：考えて打つ方が攻撃だけより勝つ" % e["name"])
		var g: Array = goals.get(e["id"], [0.0, 1.0])
		check(row["smart"][0] >= g[0] and row["smart"][0] <= g[1], "%s：勝率が目標 %d〜%d%% に入る" % [e["name"], int(g[0] * 100), int(g[1] * 100)])


## 勝率を測る（難易度の調整用）
func _simulate() -> void:
	print("")
	print("[自動対戦の勝率]")
	var decks := {
		"最初のデッキ": DB.starter_deck,
		"+強撃": DB.starter_deck + ["heavy"],
		"+強撃+祈り": DB.starter_deck + ["heavy", "prayer"],
		"+強撃+振り払う": DB.starter_deck + ["heavy", "shakeoff"],
	}
	var n := 400
	for e in DB.enemies:
		for mi in Game.INTENSITY_MULT.size():
			var mult: float = Game.INTENSITY_MULT[mi]
			for dname in decks:
				var wins := 0
				var turns := 0
				var climax := 0
				for s in n:
					var r := Bot.run_battle(DB.cards, e, decks[dname], mult, s * 7919 + 13)
					if r["result"] == "win":
						wins += 1
					turns += int(r["turns"])
					climax += int(r["climaxes"])
				print("  %s / %s / %s : 勝率 %3d%%  平均 %.1f ターン  絶頂 %.2f 回" % [
					e["name"], Game.INTENSITY_NAMES[mi], dname,
					int(100.0 * wins / n), float(turns) / n, float(climax) / n])
