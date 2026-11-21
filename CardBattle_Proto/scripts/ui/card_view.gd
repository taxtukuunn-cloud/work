class_name CardView
extends Button
## 手札の1枚。選ぶと浮き上がり、使えないときは震える。

signal activated(view: CardView)

const W := 150
const H := 212
const TYPE_COLORS := {
	"attack": Color("8a2f4a"), "skill": Color("2f4f8a"),
	"power": Color("7a5a1f"), "status": Color("55355e"),
}
const TYPE_NAMES := {"attack": "攻撃", "skill": "技", "power": "心得", "status": "誘惑"}

var card: Dictionary = {}
var def: Dictionary = {}
var playable := true
var body: PanelContainer
var live_label: Label

var _style_normal: StyleBoxFlat
var _style_focus: StyleBoxFlat
var _tween: Tween


func setup(p_card: Dictionary, p_def: Dictionary) -> CardView:
	card = p_card
	def = p_def
	custom_minimum_size = Vector2(W, H)
	size = Vector2(W, H)
	focus_mode = Control.FOCUS_ALL
	for st in ["normal", "hover", "pressed", "hover_pressed", "focus", "disabled"]:
		add_theme_stylebox_override(st, StyleBoxEmpty.new())
	_build()
	focus_entered.connect(_on_focus.bind(true))
	focus_exited.connect(_on_focus.bind(false))
	mouse_entered.connect(grab_focus)
	pressed.connect(func(): activated.emit(self))
	return self


func _build() -> void:
	var col: Color = TYPE_COLORS.get(def.get("type", "skill"), Color("444444"))
	_style_normal = UIKit.box(col.darkened(0.35), col.lightened(0.25), 12, 2, 8)
	_style_focus = UIKit.box(col.darkened(0.12), UIKit.GOLD, 12, 4, 8)
	_style_focus.shadow_color = Color(UIKit.GOLD, 0.35)
	_style_focus.shadow_size = 10
	body = PanelContainer.new()
	body.size = Vector2(W, H)
	body.mouse_filter = Control.MOUSE_FILTER_IGNORE
	body.add_theme_stylebox_override("panel", _style_normal)
	body.pivot_offset = Vector2(W / 2.0, H)
	add_child(body)

	var v := VBoxContainer.new()
	v.mouse_filter = Control.MOUSE_FILTER_IGNORE
	v.add_theme_constant_override("separation", 2)
	body.add_child(v)

	var top := HBoxContainer.new()
	top.mouse_filter = Control.MOUSE_FILTER_IGNORE
	v.add_child(top)
	var cost_text := "－" if def.get("unplayable", false) else str(int(def.get("cost", 0)))
	var cost := UIKit.outlined(UIKit.label(cost_text, 26, UIKit.GOLD, true), 6)
	cost.custom_minimum_size = Vector2(26, 0)
	top.add_child(cost)
	var nm := UIKit.label(def.get("name", ""), 19, UIKit.TEXT, true)
	nm.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	nm.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	top.add_child(nm)

	var ty := UIKit.label(TYPE_NAMES.get(def.get("type", ""), ""), 13, UIKit.SUB)
	ty.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	v.add_child(ty)
	var sep := HSeparator.new()
	sep.mouse_filter = Control.MOUSE_FILTER_IGNORE
	v.add_child(sep)
	var tx := UIKit.label(def.get("text", ""), 16, UIKit.TEXT)
	tx.autowrap_mode = TextServer.AUTOWRAP_ARBITRARY
	tx.custom_minimum_size = Vector2(W - 20, 0)
	tx.size_flags_vertical = Control.SIZE_EXPAND_FILL
	v.add_child(tx)
	# 今の高揚で実際に何点削れるか（桜井 #076 測れるようにする）
	live_label = UIKit.outlined(UIKit.label("", 17, UIKit.GOLD, true), 5)
	live_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	live_label.visible = false
	v.add_child(live_label)
	if def.get("exhaust", false) or def.get("type", "") == "power":
		var ex := UIKit.label("使うと除外", 12, UIKit.SUB)
		ex.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
		v.add_child(ex)


func set_live(text: String) -> void:
	live_label.text = text
	live_label.visible = text != ""


func set_playable(v: bool) -> void:
	playable = v
	body.modulate = Color(1, 1, 1) if v else Color(0.55, 0.55, 0.62)


func _on_focus(f: bool) -> void:
	body.add_theme_stylebox_override("panel", _style_focus if f else _style_normal)
	z_index = 10 if f else 0
	if _tween:
		_tween.kill()
	_tween = create_tween().set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT).set_parallel()
	_tween.tween_property(body, "position:y", -30.0 if f else 0.0, 0.14)
	_tween.tween_property(body, "scale", Vector2(1.08, 1.08) if f else Vector2.ONE, 0.14)


## 使えないカードを選んだとき
func shake() -> void:
	if _tween:
		_tween.kill()
	_tween = create_tween()
	for i in 5:
		_tween.tween_property(body, "position:x", 7.0 if i % 2 == 0 else -7.0, 0.035)
	_tween.tween_property(body, "position:x", 0.0, 0.035)


## 使ったときに相手の方へ飛んでいく
func fly_away() -> Tween:
	if _tween:
		_tween.kill()
	_tween = create_tween().set_parallel().set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_IN)
	_tween.tween_property(body, "position:y", -220.0, 0.18)
	_tween.tween_property(body, "modulate:a", 0.0, 0.18)
	_tween.tween_property(body, "scale", Vector2(0.8, 0.8), 0.18)
	return _tween
