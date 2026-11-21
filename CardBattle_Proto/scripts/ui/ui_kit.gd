class_name UIKit
extends RefCounted
## 色・枠・よく使う部品の作り方をまとめたもの。

const BG_TOP := Color("231231")
const BG_BOTTOM := Color("0e0814")
const PANEL := Color(0.10, 0.06, 0.14, 0.88)
const LINE := Color(1, 1, 1, 0.14)
const TEXT := Color("f4eaf8")
const SUB := Color("bfa9cc")
const NARRATION := Color("d9cbe6")
const PINK := Color("ff6fae")
const GOLD := Color("ffd66b")
const BLUE := Color("7cc4ff")
const GREEN := Color("8be0a4")
const LAVENDER := Color("b99cff")

static var font_bold: Font = preload("res://assets/fonts/NotoSansJP-Bold.ttf")


static func box(bg: Color, border: Color = LINE, radius: int = 10, bw: int = 1, margin: float = 10.0) -> StyleBoxFlat:
	var s := StyleBoxFlat.new()
	s.bg_color = bg
	s.border_color = border
	s.set_border_width_all(bw)
	s.set_corner_radius_all(radius)
	s.set_content_margin_all(margin)
	s.anti_aliasing = true
	return s


static func focus_box() -> StyleBoxFlat:
	var s := box(Color(0, 0, 0, 0), GOLD, 10, 3, 0)
	s.draw_center = false
	s.set_expand_margin_all(3)
	return s


static func build_theme() -> Theme:
	var t := Theme.new()
	t.default_font_size = 20
	t.set_stylebox("normal", "Button", box(Color("3a2147"), LINE, 8, 1, 12))
	t.set_stylebox("hover", "Button", box(Color("4e2c5f"), Color(1, 1, 1, 0.3), 8, 1, 12))
	t.set_stylebox("pressed", "Button", box(Color("632f78"), GOLD, 8, 2, 12))
	t.set_stylebox("hover_pressed", "Button", box(Color("632f78"), GOLD, 8, 2, 12))
	t.set_stylebox("focus", "Button", focus_box())
	t.set_stylebox("disabled", "Button", box(Color("241a2a"), Color(1, 1, 1, 0.05), 8, 1, 12))
	for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color", "font_hover_pressed_color"]:
		t.set_color(c, "Button", TEXT)
	t.set_color("font_disabled_color", "Button", Color(1, 1, 1, 0.35))
	t.set_stylebox("panel", "PanelContainer", box(PANEL))
	t.set_stylebox("panel", "Panel", box(PANEL))
	t.set_color("font_color", "Label", TEXT)
	t.set_stylebox("background", "ProgressBar", box(Color(0, 0, 0, 0.5), LINE, 6, 1, 0))
	t.set_stylebox("fill", "ProgressBar", box(PINK, Color(0, 0, 0, 0), 6, 0, 0))
	t.set_color("default_color", "RichTextLabel", TEXT)
	return t


static func label(text: String, font_size: int = 20, color: Color = TEXT, bold: bool = false) -> Label:
	var l := Label.new()
	l.text = text
	l.add_theme_font_size_override("font_size", font_size)
	l.add_theme_color_override("font_color", color)
	if bold:
		l.add_theme_font_override("font", font_bold)
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return l


static func outlined(l: Label, outline: int = 8, color: Color = Color(0, 0, 0, 0.85)) -> Label:
	l.add_theme_constant_override("outline_size", outline)
	l.add_theme_color_override("font_outline_color", color)
	return l


static func button(text: String, font_size: int = 22) -> Button:
	var b := Button.new()
	b.text = text
	b.add_theme_font_size_override("font_size", font_size)
	b.focus_mode = Control.FOCUS_ALL
	b.mouse_entered.connect(b.grab_focus)
	return b


static func place(c: Control, pos: Vector2, sz: Vector2) -> Control:
	c.position = pos
	c.size = sz
	return c


static func bg_gradient(top: Color = BG_TOP, bottom: Color = BG_BOTTOM) -> TextureRect:
	var g := Gradient.new()
	g.set_color(0, top)
	g.set_color(1, bottom)
	var gt := GradientTexture2D.new()
	gt.gradient = g
	gt.fill_from = Vector2(0, 0)
	gt.fill_to = Vector2(0, 1)
	gt.width = 16
	gt.height = 256
	var tr := TextureRect.new()
	tr.texture = gt
	tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	tr.stretch_mode = TextureRect.STRETCH_SCALE
	tr.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	tr.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return tr


static func bar(fill: Color) -> ProgressBar:
	var p := ProgressBar.new()
	p.show_percentage = false
	p.add_theme_stylebox_override("fill", box(fill, Color(0, 0, 0, 0), 6, 0, 0))
	p.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return p
