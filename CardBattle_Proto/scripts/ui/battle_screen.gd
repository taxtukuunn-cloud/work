class_name BattleScreen
extends Control
## 戦闘画面。計算は Battle に任せ、ここは見せ方と操作だけを受け持つ。
## 手応えの作り方は桜井スキルの 5章・7章（ヒットストップ／ヒットマーク／振動／フラッシュ）に沿う。

signal finished(result: String)

const TIER_COLORS := [Color("ff8fc0"), Color("ff5c9a"), Color("ff2a55")]

var battle: Battle
var enemy_def: Dictionary
var busy := false
var dialog_open := false
var deck_open := false
var focus_index := 0
var tutorial_step := -1  # -1 なら案内なし

var root: Control
var fx_layer: Control
var portrait: Portrait
var player_panel: PanelContainer
var e_bar: ProgressBar
var e_bar_label: Label
var e_status_label: Label
var intent_name: Label
var intent_text: Label
var intent_net: Label
var p_bar: ProgressBar
var p_bar_label: Label
var tier_label: Label
var stocks_label: Label
var block_label: Label
var energy_label: Label
var p_status_label: Label
var pile_label: Label
var log_box: VBoxContainer
var hand_box: HBoxContainer
var end_btn: Button
var beg_btn: Button
var hint_label: Label
var tutorial_panel: PanelContainer
var tutorial_label: Label
var banner: Label
var flash: ColorRect
var confirm: Control
var deck_panel: Control

var _hand_sig := ""


func setup(p_enemy: Dictionary, deck: Array) -> BattleScreen:
	enemy_def = p_enemy
	battle = Battle.new()
	battle.setup(DB.cards, enemy_def, deck, Game.intensity_mult(), -1, DB.params)
	if Game.stage == 0 and not Game.tutorial_done:
		tutorial_step = 0
	return self


func _ready() -> void:
	set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	_build()
	battle.take_events()
	_log("%sとの勝負。余裕を0にすれば勝ち" % enemy_def["name"], UIKit.SUB)
	_refresh()
	_focus_hand(0)
	_update_tutorial()
	Game.input_mode_changed.connect(func(_j):
		_update_hints()
		_update_tutorial())


func _exit_tree() -> void:
	Engine.time_scale = 1.0


func _process(_delta: float) -> void:
	# 演出中は早送りボタンで速くする（桜井 #073 遅さは罪）
	Engine.time_scale = 3.0 if (busy and Input.is_action_pressed("skip")) else 1.0
	# 限界寸前はメーターを脈打たせる（桜井 #252 状態でメーターの見せ方を変える）
	if battle.tier() >= 2 and battle.result == "":
		var k := 0.5 + 0.5 * sin(Time.get_ticks_msec() / 110.0)
		p_bar.modulate = Color(1.0 + 0.4 * k, 1.0, 1.0 + 0.2 * k)
	else:
		p_bar.modulate = Color.WHITE


# ================================================================ 画面を組む

func _build() -> void:
	add_child(UIKit.bg_gradient(Color(enemy_def.get("color", "#553366")).darkened(0.72), UIKit.BG_BOTTOM))
	root = Control.new()
	root.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	root.mouse_filter = Control.MOUSE_FILTER_PASS
	add_child(root)

	portrait = Portrait.new().setup(enemy_def)
	UIKit.place(portrait, Vector2(480, 6), Vector2(320, 376))
	root.add_child(portrait)

	# 相手の情報
	var ep := PanelContainer.new()
	UIKit.place(ep, Vector2(840, 20), Vector2(410, 150))
	root.add_child(ep)
	var ev := VBoxContainer.new()
	ep.add_child(ev)
	var nh := HBoxContainer.new()
	ev.add_child(nh)
	nh.add_child(UIKit.label(enemy_def.get("name", ""), 28, UIKit.TEXT, true))
	var et := UIKit.label("　" + enemy_def.get("title", ""), 16, UIKit.SUB)
	et.size_flags_vertical = Control.SIZE_SHRINK_END
	nh.add_child(et)
	ev.add_child(UIKit.label("余裕（0にすれば勝ち）", 14, UIKit.SUB))
	var eb := Control.new()
	eb.custom_minimum_size = Vector2(0, 26)
	ev.add_child(eb)
	e_bar = UIKit.bar(UIKit.LAVENDER)
	e_bar.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	eb.add_child(e_bar)
	e_bar_label = _bar_text(eb, 17)
	e_status_label = UIKit.label("", 16, UIKit.GOLD)
	ev.add_child(e_status_label)

	# 相手の次の行動（予告）
	var ip := PanelContainer.new()
	ip.add_theme_stylebox_override("panel", UIKit.box(Color(0.25, 0.05, 0.15, 0.9), Color(UIKit.PINK, 0.6), 10, 2, 10))
	UIKit.place(ip, Vector2(840, 182), Vector2(410, 128))
	root.add_child(ip)
	var iv := VBoxContainer.new()
	iv.add_theme_constant_override("separation", 2)
	ip.add_child(iv)
	iv.add_child(UIKit.label("次の行動", 14, UIKit.SUB))
	intent_name = UIKit.label("", 24, UIKit.PINK, true)
	iv.add_child(intent_name)
	intent_text = UIKit.label("", 17, UIKit.TEXT)
	intent_text.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	intent_text.custom_minimum_size = Vector2(385, 0)
	iv.add_child(intent_text)
	intent_net = UIKit.label("", 15, UIKit.GOLD)
	iv.add_child(intent_net)

	# 主人公の情報
	player_panel = PanelContainer.new()
	UIKit.place(player_panel, Vector2(30, 20), Vector2(410, 214))
	root.add_child(player_panel)
	var pv := VBoxContainer.new()
	pv.add_theme_constant_override("separation", 4)
	player_panel.add_child(pv)
	var ph := HBoxContainer.new()
	pv.add_child(ph)
	ph.add_child(UIKit.label("あなた", 22, UIKit.TEXT, true))
	stocks_label = UIKit.label("", 22, UIKit.PINK, true)
	stocks_label.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	stocks_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	ph.add_child(stocks_label)
	var th := HBoxContainer.new()
	pv.add_child(th)
	th.add_child(UIKit.label("興奮", 14, UIKit.SUB))
	tier_label = UIKit.label("", 16, UIKit.PINK, true)
	tier_label.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	tier_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	th.add_child(tier_label)
	var pb := Control.new()
	pb.custom_minimum_size = Vector2(0, 34)
	pv.add_child(pb)
	p_bar = UIKit.bar(TIER_COLORS[0])
	p_bar.max_value = battle.climax_at()
	p_bar.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	pb.add_child(p_bar)
	# 高揚の境目に目盛り
	for thv in DB.params["【高揚が上がる興奮】"]:
		var tick := ColorRect.new()
		tick.color = Color(1, 1, 1, 0.55)
		tick.mouse_filter = Control.MOUSE_FILTER_IGNORE
		tick.anchor_left = float(thv) / battle.climax_at()
		tick.anchor_right = tick.anchor_left
		tick.anchor_bottom = 1.0
		tick.offset_right = 2
		pb.add_child(tick)
	p_bar_label = _bar_text(pb, 19)
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 24)
	pv.add_child(row)
	energy_label = UIKit.label("", 24, UIKit.GOLD, true)
	row.add_child(energy_label)
	block_label = UIKit.label("", 24, UIKit.BLUE, true)
	row.add_child(block_label)
	p_status_label = UIKit.label("", 16, UIKit.GOLD)
	p_status_label.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	p_status_label.custom_minimum_size = Vector2(380, 0)
	pv.add_child(p_status_label)

	# 記録
	var lp := PanelContainer.new()
	UIKit.place(lp, Vector2(30, 244), Vector2(410, 138))
	lp.clip_contents = true
	root.add_child(lp)
	log_box = VBoxContainer.new()
	log_box.add_theme_constant_override("separation", 0)
	lp.add_child(log_box)

	pile_label = UIKit.label("", 15, UIKit.SUB)
	UIKit.place(pile_label, Vector2(34, 390), Vector2(420, 24))
	root.add_child(pile_label)

	# ボタン
	beg_btn = UIKit.button("", 19)
	UIKit.place(beg_btn, Vector2(840, 326), Vector2(196, 54))
	for c in ["font_color", "font_focus_color", "font_hover_color"]:
		beg_btn.add_theme_color_override(c, UIKit.PINK)
	beg_btn.pressed.connect(_open_confirm)
	root.add_child(beg_btn)
	end_btn = UIKit.button("", 20)
	UIKit.place(end_btn, Vector2(1054, 326), Vector2(196, 54))
	end_btn.pressed.connect(_on_end_turn)
	root.add_child(end_btn)

	# 案内（最初の戦闘だけ。桜井 #085 自然なチュートリアル）
	tutorial_panel = PanelContainer.new()
	tutorial_panel.add_theme_stylebox_override("panel", UIKit.box(Color(0.2, 0.14, 0.02, 0.92), UIKit.GOLD, 8, 2, 8))
	UIKit.place(tutorial_panel, Vector2(840, 388), Vector2(410, 70))
	tutorial_panel.visible = false
	root.add_child(tutorial_panel)
	tutorial_label = UIKit.label("", 16, UIKit.GOLD, true)
	tutorial_label.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	tutorial_label.custom_minimum_size = Vector2(390, 0)
	tutorial_panel.add_child(tutorial_label)

	# 手札
	hand_box = HBoxContainer.new()
	hand_box.alignment = BoxContainer.ALIGNMENT_CENTER
	UIKit.place(hand_box, Vector2(0, 470), Vector2(1280, CardView.H))
	root.add_child(hand_box)

	hint_label = UIKit.label("", 15, UIKit.SUB)
	hint_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	UIKit.place(hint_label, Vector2(0, 692), Vector2(1280, 24))
	root.add_child(hint_label)

	# 演出用
	fx_layer = Control.new()
	fx_layer.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	fx_layer.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(fx_layer)
	banner = UIKit.outlined(UIKit.label("", 34, UIKit.TEXT, true), 10)
	banner.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	UIKit.place(banner, Vector2(0, 300), Vector2(1280, 60))
	banner.modulate.a = 0.0
	fx_layer.add_child(banner)
	flash = ColorRect.new()
	flash.color = Color(UIKit.PINK, 0.0)
	flash.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	flash.mouse_filter = Control.MOUSE_FILTER_IGNORE
	fx_layer.add_child(flash)

	_update_hints()


func _bar_text(parent: Control, font_size: int) -> Label:
	var l := UIKit.outlined(UIKit.label("", font_size, UIKit.TEXT, true), 5)
	l.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	l.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	parent.add_child(l)
	return l


func _update_hints() -> void:
	beg_btn.text = "おねだり　%s" % Game.hint("surrender")
	end_btn.text = "ターン終了　%s" % Game.hint("end_turn")
	hint_label.text = "%s 選ぶ　%s 使う　%s ターン終了　%s おねだり　%s デッキ　%s 長押しで早送り" % [
		Game.hint("move"), Game.hint("accept"), Game.hint("end_turn"), Game.hint("surrender"), Game.hint("deck"), Game.hint("skip")]


# ================================================================ 案内

func _update_tutorial() -> void:
	if tutorial_step < 0:
		tutorial_panel.visible = false
		return
	var ths: Array = DB.params["【高揚が上がる興奮】"]
	var texts := [
		"カードを選んで %s で使う。攻撃で相手の「余裕」を0にすれば勝ち。" % Game.hint("accept"),
		"右上が相手の次の責め。「我慢」の忍耐で防げる。終わったら %s でターン終了。" % Game.hint("end_turn"),
		"興奮が%dを超えると「火照り」、%dで「限界寸前」。高いほど攻撃が強いが、%dで絶頂する。" % [int(ths[0]), int(ths[1]), battle.climax_at()],
		"精が尽きると負け（負けてもペナルティなし）。わざと負けたいときは %s でおねだり。" % Game.hint("surrender"),
	]
	if tutorial_step >= texts.size():
		tutorial_panel.visible = false
		return
	tutorial_label.text = texts[tutorial_step]
	if not tutorial_panel.visible:
		tutorial_panel.visible = true
		tutorial_panel.modulate.a = 0.0
		create_tween().tween_property(tutorial_panel, "modulate:a", 1.0, 0.2)


func _tutorial_advance(from_step: int) -> void:
	if tutorial_step == from_step:
		tutorial_step += 1
		Sfx.play("page")
		_update_tutorial()
		if tutorial_step >= 4:
			Game.tutorial_done = true
			Game.save()


# ================================================================ 表示の更新

func _refresh() -> void:
	e_bar.max_value = battle.e_max
	e_status_label.text = battle.status_text(battle.e_status)
	var mv := battle.current_move()
	intent_name.text = mv.get("name", "")
	intent_text.text = battle.intent_text()
	var net := battle.incoming_arousal()
	if net > 0:
		var after := battle.arousal + net
		var warn := "　絶頂する！" if after >= battle.climax_at() else ""
		intent_net.text = "このままだと興奮 +%d（%d → %d）%s" % [net, battle.arousal, after, warn]
		intent_net.add_theme_color_override("font_color", UIKit.PINK if after >= battle.climax_at() else UIKit.GOLD)
	else:
		intent_net.text = "忍耐で防ぎきれる" if _move_arouses(mv) else ""
		intent_net.add_theme_color_override("font_color", UIKit.BLUE)
	_refresh_player()
	pile_label.text = "山札 %d　捨て札 %d　除外 %d" % [battle.draw_pile.size(), battle.discard_pile.size(), battle.exhaust_pile.size()]
	_refresh_hand()


func _refresh_player() -> void:
	var a := mini(battle.arousal, battle.climax_at())
	_tween_bar(p_bar, a)
	p_bar_label.text = "%d / %d" % [a, battle.climax_at()]
	var t := battle.tier()
	p_bar.add_theme_stylebox_override("fill", UIKit.box(TIER_COLORS[t], Color(0, 0, 0, 0), 6, 0, 0))
	tier_label.text = "高揚：%s　攻撃×%s" % [battle.tier_name(), str(battle.tier_mult())]
	tier_label.add_theme_color_override("font_color", TIER_COLORS[t])
	var st := ""
	for i in battle.max_stocks:
		st += "●" if i < battle.stocks else "○"
	stocks_label.text = "精 " + st
	energy_label.text = "気力 %d/%d" % [battle.energy, battle.max_energy]
	block_label.text = "忍耐 %d" % battle.block
	p_status_label.text = battle.status_text(battle.p_status)
	e_bar_label.text = "%d / %d" % [battle.e_hp, battle.e_max]
	_tween_bar(e_bar, battle.e_hp)


func _move_arouses(mv: Dictionary) -> bool:
	for eff in mv.get("effects", []):
		if eff.get("op", "") == "arouse":
			return true
	return false


func _tween_bar(b: ProgressBar, v: float) -> void:
	create_tween().set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT).tween_property(b, "value", v, 0.25)


func _refresh_hand() -> void:
	var ids := PackedStringArray()
	for c in battle.hand:
		ids.append(str(c["uid"]))
	var sig := ",".join(ids)
	if sig != _hand_sig:
		_hand_sig = sig
		for ch in hand_box.get_children():
			hand_box.remove_child(ch)
			ch.queue_free()
		for c in battle.hand:
			var v := CardView.new().setup(c, battle.card_def(c))
			v.activated.connect(_on_card_activated)
			hand_box.add_child(v)
		var n := battle.hand.size()
		var sep := 14
		if n > 7:
			sep = int((1200.0 - n * CardView.W) / float(n - 1))
		hand_box.add_theme_constant_override("separation", sep)
	for i in hand_box.get_child_count():
		var v: CardView = hand_box.get_child(i)
		v.set_playable(battle.can_play(i))
		v.set_live(_live_text(v.def))


## 攻撃カードに「今なら何点削れるか」を出す
func _live_text(d: Dictionary) -> String:
	var total := 0
	var base := 0
	var first := true
	for eff in d.get("effects", []):
		if eff.get("op", "") != "damage":
			continue
		var hits := int(eff.get("hits", 1))
		var focus := int(battle.p_status.get("focus", 0)) if first else 0
		first = false
		total += battle.damage_value(int(eff["val"]), focus) + battle.damage_value(int(eff["val"])) * (hits - 1)
		base += int(eff["val"]) * hits
	if total == 0 or total == base:
		return ""
	return "今なら %d 削れる" % total


func _focus_hand(i: int) -> void:
	var n := hand_box.get_child_count()
	if n == 0:
		end_btn.grab_focus()
		return
	var any := false
	for k in n:
		if battle.can_play(k):
			any = true
	if not any:
		end_btn.grab_focus()
		return
	(hand_box.get_child(clampi(i, 0, n - 1)) as Control).grab_focus()


# ================================================================ 操作

func _unhandled_input(event: InputEvent) -> void:
	if OS.is_debug_build() and event is InputEventKey and event.pressed and not busy:
		if _debug_key(event.keycode):
			accept_event()
			return
	if busy or battle.result != "":
		return
	if dialog_open:
		if event.is_action_pressed("ui_cancel"):
			_close_confirm()
			accept_event()
		return
	if deck_open:
		if event.is_action_pressed("ui_cancel") or event.is_action_pressed("deck_view") or event.is_action_pressed("ui_accept"):
			_close_deck()
			accept_event()
		return
	if event.is_action_pressed("end_turn"):
		_on_end_turn()
		accept_event()
	elif event.is_action_pressed("surrender"):
		_open_confirm()
		accept_event()
	elif event.is_action_pressed("deck_view"):
		_open_deck()
		accept_event()


## 開発用の操作（桜井 #193 デバッグモード）。書き出した製品版では効かない。
func _debug_key(key: int) -> bool:
	match key:
		KEY_F2:
			battle.e_hp = 1
			_log("[開発] 相手の余裕を1にした", UIKit.SUB)
		KEY_F3:
			battle.arousal = mini(battle.arousal + 30, battle.climax_at() - 1)
			_log("[開発] 興奮+30", UIKit.SUB)
		KEY_F4:
			battle.energy += 3
			_log("[開発] 気力+3", UIKit.SUB)
		_:
			return false
	_refresh()
	return true


func _index_of(uid: int) -> int:
	for i in battle.hand.size():
		if int(battle.hand[i]["uid"]) == uid:
			return i
	return -1


func _on_card_activated(view: CardView) -> void:
	if busy or dialog_open or deck_open or battle.result != "":
		return
	var idx := _index_of(int(view.card["uid"]))
	if not battle.can_play(idx):
		# 押して何も起きない、を作らない（桜井 #104）
		view.shake()
		Sfx.play("deny")
		_log(battle.why_unplayable(idx), UIKit.SUB)
		return
	busy = true
	focus_index = idx
	Sfx.play("play")
	await view.fly_away().finished
	battle.play(idx)
	await _play_events(battle.take_events())
	_refresh()
	busy = false
	_tutorial_advance(0)
	if await _check_end():
		return
	_focus_hand(focus_index)


func _on_end_turn() -> void:
	if busy or dialog_open or deck_open or battle.result != "":
		return
	busy = true
	Sfx.play("confirm")
	end_btn.release_focus()
	var tw := create_tween().set_parallel()
	for v in hand_box.get_children():
		tw.tween_property(v, "modulate:a", 0.0, 0.12)
	await tw.finished
	battle.end_turn()
	await _play_events(battle.take_events())
	_refresh()
	busy = false
	_tutorial_advance(1)
	if tutorial_step == 2 and battle.turn >= 3:
		_tutorial_advance(2)
	elif tutorial_step == 3 and battle.turn >= 4:
		_tutorial_advance(3)
	if await _check_end():
		return
	_focus_hand(0)


func _check_end() -> bool:
	if battle.result == "":
		return false
	busy = true
	tutorial_panel.visible = false
	if battle.result == "win":
		await _win_fx()
	elif battle.surrendered:
		await _banner("……おねがい、します……", UIKit.PINK, 0.8)
	else:
		await _banner("もう……我慢できない……", UIKit.PINK, 1.0)
	if tutorial_step >= 0:
		Game.tutorial_done = true
		Game.save()
	finished.emit(battle.result)
	return true


# ================================================================ おねだりの確認

func _open_confirm() -> void:
	if busy or dialog_open or battle.result != "":
		return
	dialog_open = true
	Sfx.play("confirm")
	confirm = Control.new()
	confirm.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.6)
	dim.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	confirm.add_child(dim)
	var p := PanelContainer.new()
	p.add_theme_stylebox_override("panel", UIKit.box(Color("2a1433"), UIKit.PINK, 14, 2, 24))
	UIKit.place(p, Vector2(340, 220), Vector2(600, 250))
	confirm.add_child(p)
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 16)
	p.add_child(v)
	v.add_child(UIKit.label("おねだりしますか？", 30, UIKit.PINK, true))
	var d := UIKit.label("自分から負けを選んで、%sの敗北シーンに進みます。\nペナルティはありません。あとで同じ相手に挑み直せます。" % enemy_def["name"], 18, UIKit.TEXT)
	d.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	d.custom_minimum_size = Vector2(550, 0)
	v.add_child(d)
	var h := HBoxContainer.new()
	h.alignment = BoxContainer.ALIGNMENT_CENTER
	h.add_theme_constant_override("separation", 30)
	v.add_child(h)
	var yes := UIKit.button("おねだりする", 22)
	yes.custom_minimum_size = Vector2(220, 56)
	for c in ["font_color", "font_focus_color", "font_hover_color"]:
		yes.add_theme_color_override(c, UIKit.PINK)
	var no := UIKit.button("やめる（%s）" % Game.hint("cancel"), 22)
	no.custom_minimum_size = Vector2(220, 56)
	h.add_child(yes)
	h.add_child(no)
	yes.pressed.connect(func():
		_close_confirm()
		busy = true
		battle.surrender()
		battle.take_events()
		_check_end())
	no.pressed.connect(_close_confirm)
	add_child(confirm)
	no.grab_focus.call_deferred()


func _close_confirm() -> void:
	dialog_open = false
	if confirm:
		confirm.queue_free()
		confirm = null
	if battle.result == "":
		_focus_hand(focus_index)


# ================================================================ デッキを見る

func _open_deck() -> void:
	deck_open = true
	Sfx.play("confirm")
	deck_panel = Control.new()
	deck_panel.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.7)
	dim.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	deck_panel.add_child(dim)
	var p := PanelContainer.new()
	UIKit.place(p, Vector2(240, 80), Vector2(800, 560))
	deck_panel.add_child(p)
	var v := VBoxContainer.new()
	p.add_child(v)
	v.add_child(UIKit.label("山札の中身（順番はわからない）", 24, UIKit.TEXT, true))
	var counts := {}
	for c in battle.draw_pile:
		var nm: String = battle.card_def(c).get("name", c["id"])
		counts[nm] = int(counts.get(nm, 0)) + 1
	var names := counts.keys()
	names.sort()
	var lines := PackedStringArray()
	for nm in names:
		lines.append("%s ×%d" % [nm, counts[nm]])
	v.add_child(UIKit.label("\n".join(lines) if lines.size() > 0 else "（空っぽ。捨て札を混ぜ直して引く）", 20))
	v.add_child(UIKit.label("\n捨て札 %d枚　除外 %d枚" % [battle.discard_pile.size(), battle.exhaust_pile.size()], 18, UIKit.SUB))
	v.add_child(UIKit.label("%s で閉じる" % Game.hint("cancel"), 16, UIKit.SUB))
	add_child(deck_panel)


func _close_deck() -> void:
	deck_open = false
	if deck_panel:
		deck_panel.queue_free()
		deck_panel = null
	_focus_hand(focus_index)


# ================================================================ 演出

func _wait(t: float) -> void:
	await get_tree().create_timer(t).timeout


func _frames(n: float) -> void:
	await _wait(n / 60.0)


func _log(text: String, col: Color = UIKit.TEXT) -> void:
	if text == "":
		return
	var l := UIKit.label(text, 15, col)
	l.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	l.custom_minimum_size = Vector2(385, 0)
	log_box.add_child(l)
	while log_box.get_child_count() > 4 or (log_box.get_child_count() > 1 and log_box.get_combined_minimum_size().y > 118):
		var old := log_box.get_child(0)
		log_box.remove_child(old)
		old.queue_free()


func _float(text: String, pos: Vector2, col: Color, font_size: int = 30) -> void:
	var l := UIKit.outlined(UIKit.label(text, font_size, col, true), 8)
	l.position = pos - Vector2(100, 20)
	l.size = Vector2(200, 40)
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	fx_layer.add_child(l)
	var tw := l.create_tween().set_parallel().set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
	l.scale = Vector2(1.5, 1.5)
	l.pivot_offset = Vector2(100, 20)
	tw.tween_property(l, "scale", Vector2.ONE, 0.12)
	tw.tween_property(l, "position:y", l.position.y - 60.0, 0.8)
	tw.tween_property(l, "modulate:a", 0.0, 0.45).set_delay(0.4)
	tw.chain().tween_callback(l.queue_free)


## 画面振動（桜井 #103：大中小で揺れ方そのものを変える。小は縦だけ、中は縦主体、大は横主体）
func _shake(level: int) -> void:
	var amp: float = [4.0, 8.0, 15.0][level]
	var frames: int = [6, 10, 18][level]
	var tw := create_tween()
	for i in frames:
		var k := amp * (1.0 - float(i) / frames)
		var sgn := 1.0 if i % 2 == 0 else -1.0
		var off := Vector2.ZERO
		match level:
			0:
				off = Vector2(0, k * sgn)
			1:
				off = Vector2(randf_range(-k, k) * 0.35, k * sgn)
			2:
				off = Vector2(k * (1.0 if (i / 2) % 2 == 0 else -1.0), randf_range(-k, k) * 0.35)
		tw.tween_property(root, "position", off, 1.0 / 60.0)
	tw.tween_property(root, "position", Vector2.ZERO, 1.0 / 60.0)


## 画面フラッシュ（桜井 #221：明るい色と暗い色を交互に）
func _flash(col: Color, strength: float = 0.8) -> void:
	var seq := [Color(col, strength), Color(0, 0, 0, strength * 0.55), Color(col, strength * 0.55),
		Color(0, 0, 0, strength * 0.3), Color(col, strength * 0.25), Color(col, 0.0)]
	var tw := create_tween()
	for c in seq:
		tw.tween_property(flash, "color", c, 2.0 / 60.0)


func _banner(text: String, col: Color = UIKit.TEXT, hold: float = 0.6) -> void:
	banner.text = text
	banner.add_theme_color_override("font_color", col)
	banner.scale = Vector2(1.25, 1.25)
	banner.pivot_offset = Vector2(640, 30)
	var tw := create_tween()
	tw.tween_property(banner, "modulate:a", 1.0, 0.08)
	tw.parallel().tween_property(banner, "scale", Vector2.ONE, 0.12).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
	tw.tween_interval(hold)
	tw.tween_property(banner, "modulate:a", 0.0, 0.15)
	await tw.finished


func _enemy_center() -> Vector2:
	return portrait.position + Vector2(portrait.size.x * 0.5, portrait.size.y * 0.4)


func _player_bar_center() -> Vector2:
	return Vector2(235, 112)


func _play_events(evs: Array) -> void:
	for e in evs:
		match e["type"]:
			"enemy_damage":
				var v := int(e["val"])
				var big := v >= 15
				# ヒットストップ（桜井 #003/#047）：強いほど長く止める。受けた側を大きく、与えた側を小さく震わせる
				portrait.hit(0.6 + v / 14.0)
				HitMark.spawn(fx_layer, _enemy_center() + Vector2(randf_range(-50, 50), randf_range(-40, 30)), 44.0 + v * 1.6, TIER_COLORS[int(e.get("tier", 0))].lightened(0.3))
				Sfx.play("hit_big" if big else "hit", 1.0 + randf_range(-0.05, 0.05))
				_shake(1 if big else 0)
				_float("-%d" % v, _enemy_center() + Vector2(randf_range(-40, 40), -60), UIKit.TEXT, 46 if big else 36)
				_refresh_player()
				await _frames(clampf(4.0 + v / 2.0, 4.0, 16.0))
				await _frames(4)
			"block":
				_float("忍耐+%d" % int(e["val"]), Vector2(330, 180), UIKit.BLUE, 24)
				Sfx.play("block")
				_refresh_player()
				await _frames(4)
			"blocked":
				_float("%d防いだ" % int(e["val"]), Vector2(330, 180), UIKit.BLUE, 26)
				Sfx.play("block")
				await _frames(8)
			"calm":
				if int(e["val"]) > 0:
					_float("-%d" % int(e["val"]), _player_bar_center(), UIKit.GREEN, 28)
				_refresh_player()
				await _frames(5)
			"arousal":
				var v := int(e["val"])
				var from_enemy: bool = e.get("from_enemy", false)
				_float("+%d" % v, _player_bar_center() + Vector2(randf_range(-30, 30), 0), UIKit.PINK, 30 if v < 20 else 42)
				if from_enemy:
					Sfx.play("arouse_big" if v >= 20 else "arouse")
					_shake(1 if v >= 20 else 0)
					_shake_panel(player_panel, v)
				_refresh_player()
				await _frames(14 if from_enemy else 5)
			"energy":
				_refresh_player()
			"tier":
				var t := int(e["tier"])
				_refresh_player()
				if e.get("up", false):
					Sfx.play("tier_up")
					_float("%s！ 攻撃×%s" % [battle.tier_name(t), str(battle.tier_mult(t))], Vector2(235, 70), TIER_COLORS[t], 28)
					_log("高揚が「%s」に上がった。攻撃×%s" % [battle.tier_name(t), str(battle.tier_mult(t))], TIER_COLORS[t])
					if tutorial_step == 2:
						_tutorial_advance(2)
				await _frames(8)
			"climax":
				await _climax_fx(e)
			"enemy_move":
				_log("%sの「%s」" % [enemy_def["name"], e["name"]], UIKit.PINK)
				await _banner("%sの「%s」" % [enemy_def["name"], e["name"]], UIKit.PINK, 0.3)
			"add_card":
				var nm: String = DB.cards.get(e["card"], {}).get("name", e["card"])
				var where: String = {"draw": "山札", "discard": "捨て札", "hand": "手札"}.get(e["to"], "")
				_log("「%s」×%d が%sに混ぜられた" % [nm, int(e["n"]), where], UIKit.LAVENDER)
			"status":
				var who: String = "あなた" if e["who"] == "player" else enemy_def["name"]
				_log("%sは%sになった（%s）" % [who, Battle.STATUS_NAMES.get(e["id"], e["id"]), Battle.STATUS_HELP.get(e["id"], "")], UIKit.GOLD)
			"enemy_heal":
				if int(e["val"]) > 0:
					_float("+%d" % int(e["val"]), _enemy_center(), UIKit.LAVENDER, 28)
					_refresh_player()
					await _frames(8)
			"log":
				_log(e["text"], UIKit.SUB)
			"turn_start":
				_log("―― ターン %d ――" % int(e["turn"]), UIKit.SUB)
			"reshuffle":
				_log("捨て札を混ぜて山札に戻した", UIKit.SUB)
			"phase2":
				await _banner("%sの目つきが変わった……" % enemy_def["name"], UIKit.LAVENDER, 0.7)
	_refresh()


## 責めを受けたときにパネルを縦に小さく揺らす（受けた側を震わせる）
func _shake_panel(p: Control, v: int) -> void:
	var base := Vector2(30, 20)
	var amp := clampf(v / 4.0, 2.0, 9.0)
	var tw := create_tween()
	for i in 6:
		tw.tween_property(p, "position", base + Vector2(0, amp * (1.0 - i / 6.0) * (1 if i % 2 == 0 else -1)), 1.0 / 60.0)
	tw.tween_property(p, "position", base, 1.0 / 60.0)


func _climax_fx(e: Dictionary) -> void:
	_tween_bar(p_bar, battle.climax_at())
	p_bar_label.text = "%d / %d" % [battle.climax_at(), battle.climax_at()]
	await _frames(10)
	# 「やられた」瞬間は止めて、明暗のフラッシュと大きな揺れ（桜井 #003）
	Sfx.play("climax")
	_flash(UIKit.PINK, 0.9)
	_shake(2)
	await _frames(30)
	await _banner("絶頂……！", UIKit.PINK, 0.6)
	_log("絶頂して、精が1つ減った（残り%d）。%sが余裕を%d取り戻した" % [int(e["stocks"]), enemy_def["name"], int(e["heal"])], UIKit.PINK)
	_refresh_player()
	await _frames(10)


## 勝ったときに褒める（桜井 #095 ほめてやれ！）
func _win_fx() -> void:
	Sfx.play("win")
	_flash(UIKit.GOLD, 0.6)
	portrait.hit(1.5)
	await _frames(20)
	var praise := PackedStringArray()
	if battle.climaxes == 0:
		praise.append("一度も果てずに勝った！　鋼の理性")
	elif battle.stocks == 1:
		praise.append("精が残り1つ。ぎりぎりで耐えきった！")
	if battle.best_tier >= 2:
		praise.append("限界寸前の高揚で押しきった！")
	if battle.turn <= 4:
		praise.append("%dターンの速攻！" % battle.turn)
	if praise.is_empty():
		praise.append("よく耐えた！")
	await _banner("%sの余裕を崩した！" % enemy_def["name"], UIKit.GOLD, 0.5)
	var p := PanelContainer.new()
	p.add_theme_stylebox_override("panel", UIKit.box(Color(0.15, 0.1, 0.02, 0.95), UIKit.GOLD, 14, 2, 22))
	UIKit.place(p, Vector2(390, 230), Vector2(500, 0))
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 6)
	p.add_child(v)
	v.add_child(UIKit.label("勝利", 34, UIKit.GOLD, true))
	v.add_child(UIKit.label("ターン %d　／　絶頂 %d回　／　最高の高揚：%s" % [battle.turn, battle.climaxes, battle.tier_name(battle.best_tier)], 17, UIKit.TEXT))
	for s in praise:
		v.add_child(UIKit.label(s, 20, UIKit.PINK, true))
	v.add_child(UIKit.label("%s で次へ" % Game.hint("accept"), 15, UIKit.SUB))
	fx_layer.add_child(p)
	p.modulate.a = 0.0
	create_tween().tween_property(p, "modulate:a", 1.0, 0.15)
	# 決定で進む。放っておいても数秒で進む
	var t := 0.0
	await _frames(12)
	while t < 4.0:
		if Input.is_action_just_pressed("ui_accept") or Input.is_action_pressed("skip"):
			break
		await get_tree().process_frame
		t += get_process_delta_time()
	Sfx.play("confirm")
