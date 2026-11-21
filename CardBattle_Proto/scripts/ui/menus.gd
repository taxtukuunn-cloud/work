class_name Menus
extends RefCounted
## タイトル・報酬・敗北後・回想・設定の画面。どれも小さいので1つにまとめた。


## 縦に並んだボタンのメニューを作り、最初のボタンを選んだ状態にする
static func vmenu(parent: Control, pos: Vector2, width: float, items: Array) -> Array:
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 12)
	UIKit.place(v, pos, Vector2(width, 0))
	parent.add_child(v)
	var buttons := []
	for it in items:
		var b := UIKit.button(it[0], 24)
		b.custom_minimum_size = Vector2(width, 56)
		b.pressed.connect(it[1])
		v.add_child(b)
		buttons.append(b)
	if buttons.size() > 0:
		(buttons[0] as Button).grab_focus.call_deferred()
	return buttons


static func screen(top: Color = UIKit.BG_TOP, bottom: Color = UIKit.BG_BOTTOM) -> Control:
	var c := Control.new()
	c.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	c.add_child(UIKit.bg_gradient(top, bottom))
	return c


# ---------------------------------------------------------------- タイトル

static func title(on_start: Callable, on_gallery: Callable, on_settings: Callable, on_quit: Callable) -> Control:
	var s := screen()
	var queen := Portrait.new().setup(DB.enemies[DB.enemies.size() - 1])
	queen.modulate = Color(1, 1, 1, 0.55)
	UIKit.place(queen, Vector2(700, 40), Vector2(520, 640))
	s.add_child(queen)
	var t := UIKit.outlined(UIKit.label("淫魔の誘惑デッキ", 64, UIKit.PINK, true), 12)
	UIKit.place(t, Vector2(80, 110), Vector2(800, 90))
	s.add_child(t)
	var sub := UIKit.label("（仮）　試作版　―― 逆転なし・負けてもペナルティなし", 20, UIKit.SUB)
	UIKit.place(sub, Vector2(86, 200), Vector2(800, 30))
	s.add_child(sub)
	var gc := Game.gallery_count()
	var btns := vmenu(s, Vector2(90, 300), 320, [
		["はじめから", on_start], ["回想　%d / %d" % [gc.x, gc.y], on_gallery], ["設定", on_settings], ["終わる", on_quit],
	])
	# メニューにヘルプを（桜井 #227）
	var help := UIKit.label("", 17, UIKit.SUB)
	UIKit.place(help, Vector2(90, 580), Vector2(600, 30))
	s.add_child(help)
	var helps := ["最初の相手から遊ぶ。負けてもペナルティなし", "見たシーンをもう一度見る", "責めの強さ・文字の速さ・音量・ボタン", "ゲームを閉じる"]
	for i in btns.size():
		(btns[i] as Button).focus_entered.connect(func(): help.text = helps[i])
	var note := UIKit.label("登場人物はすべて成人です。", 14, UIKit.SUB)
	UIKit.place(note, Vector2(90, 680), Vector2(500, 24))
	s.add_child(note)
	return s


# ---------------------------------------------------------------- 報酬

static func reward(rng: RandomNumberGenerator, on_pick: Callable, rare_guaranteed: bool = false) -> Control:
	var s := screen()
	var t := UIKit.label("報酬 ―― カードを1枚、デッキに加える", 34, UIKit.GOLD, true)
	UIKit.place(t, Vector2(0, 70), Vector2(1280, 50))
	t.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	s.add_child(t)
	var sub := UIKit.label("今のデッキ %d枚。加えないのもあり。" % Game.deck.size(), 18, UIKit.SUB)
	UIKit.place(sub, Vector2(0, 126), Vector2(1280, 30))
	sub.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	s.add_child(sub)

	var commons := []
	var rares := []
	for id in DB.reward_pool():
		if DB.cards[id].get("rarity", "") == "rare":
			rares.append(id)
		else:
			commons.append(id)
	var picks := []
	while picks.size() < 3:
		var from := rares if (rng.randf() < Game.rare_chance() or (rare_guaranteed and picks.is_empty())) else commons
		var id: String = from[rng.randi_range(0, from.size() - 1)]
		if id not in picks:
			picks.append(id)

	var h := HBoxContainer.new()
	h.alignment = BoxContainer.ALIGNMENT_CENTER
	h.add_theme_constant_override("separation", 60)
	UIKit.place(h, Vector2(0, 230), Vector2(1280, CardView.H))
	s.add_child(h)
	var first: Control = null
	for i in picks.size():
		var id: String = picks[i]
		var col := VBoxContainer.new()
		col.add_theme_constant_override("separation", 40)
		h.add_child(col)
		var cv := CardView.new().setup({"uid": -1 - i, "id": id}, DB.cards[id])
		cv.activated.connect(func(_v): on_pick.call(id))
		col.add_child(cv)
		var rr := UIKit.label("レア" if DB.cards[id].get("rarity", "") == "rare" else "", 16, UIKit.GOLD, true)
		rr.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		col.add_child(rr)
		if first == null:
			first = cv
	var skip := UIKit.button("加えない", 22)
	UIKit.place(skip, Vector2(540, 560), Vector2(200, 56))
	skip.pressed.connect(func(): on_pick.call(""))
	s.add_child(skip)
	first.grab_focus.call_deferred()
	return s


# ---------------------------------------------------------------- 敗北のあと

static func lose(enemy_name: String, losses: int, on_retry: Callable, on_title: Callable, on_easier: Callable) -> Control:
	var s := screen(Color("3a1030"), Color("12060f"))
	var t := UIKit.outlined(UIKit.label("敗北", 64, UIKit.PINK, true), 10)
	UIKit.place(t, Vector2(0, 150), Vector2(1280, 90))
	t.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	s.add_child(t)
	var d := UIKit.label("ペナルティはありません。デッキはそのままで、%sにもう一度挑めます。\n見たシーンは回想に追加されました。" % enemy_name, 20, UIKit.TEXT)
	UIKit.place(d, Vector2(0, 250), Vector2(1280, 70))
	d.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	s.add_child(d)
	var items := [["もう一度挑む", on_retry]]
	# 負け続けたら、屈辱のない形で責めを弱める道を出す（桜井 #211）
	var th := int(DB.params["【責めを弱めるよう勧める負けの回数】"])
	if losses >= th and int(Game.settings["intensity"]) > 0:
		var now: String = Game.INTENSITY_NAMES[int(Game.settings["intensity"])]
		var lower: String = Game.INTENSITY_NAMES[int(Game.settings["intensity"]) - 1]
		items.append(["少しやさしくしてもらって挑む（%s→%s）" % [now, lower], on_easier])
	items.append(["タイトルへ", on_title])
	vmenu(s, Vector2(390, 360), 500, items)
	return s


# ---------------------------------------------------------------- 回想

static func gallery(on_play: Callable, on_back: Callable) -> Control:
	var s := screen()
	var seen := 0
	var total := 0
	var t := UIKit.label("回想", 40, UIKit.PINK, true)
	UIKit.place(t, Vector2(80, 40), Vector2(400, 60))
	s.add_child(t)
	var grid := GridContainer.new()
	grid.columns = 4
	grid.add_theme_constant_override("h_separation", 16)
	grid.add_theme_constant_override("v_separation", 16)
	UIKit.place(grid, Vector2(80, 140), Vector2(1120, 400))
	s.add_child(grid)
	var first: Button = null
	var kinds := [["_lose1", "敗北 その1"], ["_lose2", "敗北 その2"], ["_win", "見送り（勝利）"]]
	for e in DB.enemies:
		var nl := UIKit.label("%s\n%s" % [e["name"], e["title"]], 20, UIKit.TEXT, true)
		nl.custom_minimum_size = Vector2(220, 90)
		nl.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		grid.add_child(nl)
		for k in kinds:
			var sid: String = e["id"] + k[0]
			total += 1
			var open := Game.is_unlocked(sid)
			if open:
				seen += 1
			var b := UIKit.button(("%s\n%s" % [k[1], DB.scenes[sid]["title"].split("：")[-1]]) if open else "？？？", 18)
			b.custom_minimum_size = Vector2(270, 90)
			if open:
				b.pressed.connect(func(): on_play.call(sid))
			else:
				b.add_theme_color_override("font_color", Color(1, 1, 1, 0.35))
				b.add_theme_color_override("font_focus_color", Color(1, 1, 1, 0.5))
			grid.add_child(b)
			if first == null:
				first = b
	var c := UIKit.label("見たシーン %d / %d" % [seen, total], 20, UIKit.SUB)
	UIKit.place(c, Vector2(400, 56), Vector2(400, 40))
	s.add_child(c)
	var back := UIKit.button("戻る", 22)
	UIKit.place(back, Vector2(80, 600), Vector2(200, 56))
	back.pressed.connect(on_back)
	s.add_child(back)
	first.grab_focus.call_deferred()
	return s


# ---------------------------------------------------------------- 設定

static func settings(on_back: Callable) -> Control:
	var s := screen()
	var t := UIKit.label("設定", 40, UIKit.PINK, true)
	UIKit.place(t, Vector2(80, 40), Vector2(400, 60))
	s.add_child(t)
	var help := UIKit.label("", 18, UIKit.SUB)
	help.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	UIKit.place(help, Vector2(560, 150), Vector2(620, 200))
	s.add_child(help)

	var rows := [
		["責めの強さ", "intensity", Game.INTENSITY_NAMES, "受ける興奮の量が変わります。\nあまあま 0.75倍／ふつう 1倍／はげしい 1.3倍。\n強いほど、勝ったときの報酬にレアカードが出やすい。\n負けたい人は「はげしい」、じっくり勝ちたい人は「あまあま」。"],
		["文字の速さ", "text_speed", Game.TEXT_SPEED_NAMES, "シーンの文字が出る速さ。"],
		["音の大きさ", "volume", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "効果音の大きさ。"],
		["決定とキャンセル", "swap_ab", ["Ⓐ決定 Ⓑ戻る", "Ⓑ決定 Ⓐ戻る"], "コントローラーの決定ボタンと戻るボタンを入れ替えます。"],
		["回想をすべて開放", "unlock_all", ["オフ", "オン"], "オンにすると、まだ見ていないシーンも回想で見られます。"],
	]
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 12)
	UIKit.place(v, Vector2(80, 150), Vector2(440, 0))
	s.add_child(v)
	var first: Button = null
	for r in rows:
		var b := UIKit.button("", 22)
		b.custom_minimum_size = Vector2(440, 56)
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		var key: String = r[1]
		var names: Array = r[2]
		var label_text: String = r[0]
		var explain: String = r[3]
		var upd := func():
			var cur = Game.settings[key]
			var i := (1 if cur else 0) if typeof(cur) == TYPE_BOOL else int(cur)
			b.text = "%s　◀ %s ▶" % [label_text, names[i]]
		var step := func(d: int):
			var cur = Game.settings[key]
			if typeof(cur) == TYPE_BOOL:
				Game.settings[key] = not cur
			else:
				Game.settings[key] = posmod(int(cur) + d, names.size())
			Game.save()
			if key == "swap_ab":
				Game.apply_button_layout()
			Sfx.play("confirm")
			upd.call()
		upd.call()
		b.pressed.connect(func(): step.call(1))
		b.focus_entered.connect(func(): help.text = explain)
		b.gui_input.connect(func(ev: InputEvent):
			if ev.is_action_pressed("ui_right"):
				step.call(1)
				b.accept_event()
			elif ev.is_action_pressed("ui_left"):
				step.call(-1)
				b.accept_event())
		v.add_child(b)
		if first == null:
			first = b
	var back := UIKit.button("戻る", 22)
	back.custom_minimum_size = Vector2(440, 56)
	back.pressed.connect(on_back)
	back.focus_entered.connect(func(): help.text = "")
	v.add_child(back)
	first.grab_focus.call_deferred()
	return s
