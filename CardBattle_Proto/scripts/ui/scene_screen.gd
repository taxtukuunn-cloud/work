class_name SceneScreen
extends Control
## 会話とHシーンを1行ずつ見せる画面。

signal finished

var scene_id := ""
var data: Dictionary = {}
var lines: Array = []
var idx := -1
var enemy_def: Dictionary = {}

var portrait: Portrait
var name_label: Label
var text_label: RichTextLabel
var next_mark: Label
var hint_label: Label
var _typing: Tween
var _done := false
var _skip_t := 0.0


func setup(id: String) -> SceneScreen:
	scene_id = id
	data = DB.scenes.get(id, {"title": id, "lines": [{"who": "", "text": "（シーン %s がありません）" % id}]})
	lines = data.get("lines", [])
	enemy_def = DB.enemy(data.get("enemy", ""))
	return self


func _ready() -> void:
	set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var col := Color(enemy_def.get("color", "#2a1a33"))
	add_child(UIKit.bg_gradient(col.darkened(0.6), col.darkened(0.88)))
	if not enemy_def.is_empty():
		portrait = Portrait.new().setup(enemy_def)
		UIKit.place(portrait, Vector2(400, 0), Vector2(480, 520))
		add_child(portrait)
	var title := UIKit.outlined(UIKit.label(data.get("title", ""), 18, UIKit.SUB), 4)
	UIKit.place(title, Vector2(24, 16), Vector2(600, 30))
	add_child(title)

	var box := PanelContainer.new()
	box.add_theme_stylebox_override("panel", UIKit.box(Color(0.07, 0.03, 0.1, 0.9), Color(1, 1, 1, 0.18), 14, 2, 22))
	UIKit.place(box, Vector2(60, 478), Vector2(1160, 212))
	add_child(box)
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 6)
	box.add_child(v)
	name_label = UIKit.label("", 24, UIKit.PINK, true)
	v.add_child(name_label)
	text_label = RichTextLabel.new()
	text_label.bbcode_enabled = false
	text_label.fit_content = true
	text_label.scroll_active = false
	text_label.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	text_label.add_theme_font_size_override("normal_font_size", 23)
	text_label.custom_minimum_size = Vector2(1110, 120)
	text_label.mouse_filter = Control.MOUSE_FILTER_IGNORE
	v.add_child(text_label)

	next_mark = UIKit.label("▼", 18, UIKit.GOLD)
	UIKit.place(next_mark, Vector2(1186, 660), Vector2(24, 24))
	add_child(next_mark)
	hint_label = UIKit.label("", 14, UIKit.SUB)
	hint_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	UIKit.place(hint_label, Vector2(600, 694), Vector2(620, 22))
	add_child(hint_label)
	_update_hints()
	Game.input_mode_changed.connect(func(_j): _update_hints())
	_next()


func _update_hints() -> void:
	hint_label.text = "%s 次へ　　%s 長押しで早送り　　%s 飛ばす" % [Game.hint("accept"), Game.hint("skip"), Game.hint("cancel")]


func _next() -> void:
	idx += 1
	if idx >= lines.size():
		_finish()
		return
	var l: Dictionary = lines[idx]
	var who: String = l.get("who", "")
	name_label.text = who
	name_label.visible = who != ""
	text_label.text = l.get("text", "")
	text_label.add_theme_color_override("default_color", UIKit.TEXT if who != "" else UIKit.NARRATION)
	if who != "" and portrait:
		portrait.hit(0.25)
	var cps := Game.text_cps()
	if _typing:
		_typing.kill()
	if cps <= 0.0 or Input.is_action_pressed("skip"):
		text_label.visible_ratio = 1.0
	else:
		text_label.visible_ratio = 0.0
		_typing = create_tween()
		_typing.tween_property(text_label, "visible_ratio", 1.0, text_label.text.length() / cps)


func _advance() -> void:
	if _done:
		return
	if _typing and _typing.is_running():
		_typing.kill()
		text_label.visible_ratio = 1.0
		return
	Sfx.play("page")
	_next()


func _finish() -> void:
	if _done:
		return
	_done = true
	finished.emit()


func _unhandled_input(event: InputEvent) -> void:
	if _done:
		return
	if event.is_action_pressed("ui_accept"):
		_advance()
		accept_event()
	elif event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		_advance()
		accept_event()
	elif event.is_action_pressed("ui_cancel"):
		_finish()
		accept_event()


func _process(delta: float) -> void:
	next_mark.modulate.a = 0.4 + 0.6 * absf(sin(Time.get_ticks_msec() / 300.0))
	next_mark.visible = not (_typing and _typing.is_running())
	if Input.is_action_pressed("skip") and not _done:
		_skip_t += delta
		if _skip_t > 0.07:
			_skip_t = 0.0
			if _typing and _typing.is_running():
				_typing.kill()
				text_label.visible_ratio = 1.0
			else:
				_next()
