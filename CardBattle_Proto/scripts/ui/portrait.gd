class_name Portrait
extends Control
## 仮の立ち絵。本番の絵ができるまで、図形で描いた人影を出しておく。
## 差し替えるときは texture にPNGを入れれば、そちらが表示される。

var shape := "succubus"
var body_col := Color("e07aa8")
var hair_col := Color("f4c1d9")
var skin := Color("f3d3c6")
var texture: Texture2D = null

var _t := 0.0
var _shake := 0.0
var _punch := 0.0
var _flash := 0.0


func setup(enemy: Dictionary) -> Portrait:
	shape = enemy.get("shape", "succubus")
	body_col = Color(enemy.get("color", "#e07aa8"))
	hair_col = Color(enemy.get("hair", "#f4c1d9"))
	var tex_path := "res://assets/portraits/%s.png" % enemy.get("id", "")
	if ResourceLoader.exists(tex_path):
		texture = load(tex_path)
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	return self


## 攻撃を受けたときの揺れ（桜井 #047：受けた側を大きく震わせ、大→小に収束）
func hit(strength: float = 1.0) -> void:
	_shake = clampf(strength, 0.3, 1.8)
	_punch = 1.0
	_flash = 1.0


func _process(delta: float) -> void:
	_t += delta
	_shake = maxf(0.0, _shake - delta * 3.5)
	_punch = maxf(0.0, _punch - delta * 5.0)
	_flash = maxf(0.0, _flash - delta * 8.0)
	# 当たった瞬間は白く、次に暗く（桜井 #221 明暗を交互に）
	if _flash > 0.6:
		modulate = Color(1.8, 1.8, 1.8)
	elif _flash > 0.3:
		modulate = Color(0.55, 0.5, 0.6)
	else:
		modulate = Color(1, 1, 1)
	queue_redraw()


func _off() -> Vector2:
	# 地上の相手なので横に揺らす（桜井 #047）
	var jitter := (1.0 if int(_t * 60.0) % 2 == 0 else -1.0) * _shake * _shake * 9.0
	return Vector2(jitter, sin(_t * 1.7) * 4.0)


func _p(x: float, y: float) -> Vector2:
	var c := Vector2(0.5, 0.6)
	var s := 1.0 - _punch * 0.04
	return Vector2((c.x + (x - c.x) * s) * size.x, (c.y + (y - c.y) * s) * size.y) + _off()


func _poly(pts: Array, col: Color) -> void:
	var arr := PackedVector2Array()
	for p in pts:
		arr.append(_p(p[0], p[1]))
	draw_colored_polygon(arr, col)


func _mirror(pts: Array) -> Array:
	var out := []
	for p in pts:
		out.append([1.0 - p[0], p[1]])
	return out


func _line(pts: Array, col: Color, w: float) -> void:
	var arr := PackedVector2Array()
	for p in pts:
		arr.append(_p(p[0], p[1]))
	draw_polyline(arr, col, w * size.x, true)


func _draw() -> void:
	if texture:
		var r := Rect2(_off(), size)
		draw_texture_rect(texture, r, false)
		return
	var cx := size.x * 0.5
	# 後ろの光
	draw_circle(Vector2(cx, size.y * 0.45) + _off(), size.x * 0.46, Color(body_col, 0.10))
	draw_circle(Vector2(cx, size.y * 0.45) + _off(), size.x * 0.32, Color(body_col, 0.14))
	var dark := body_col.darkened(0.55)
	# 翼
	if shape == "succubus" or shape == "queen":
		var big := 1.25 if shape == "queen" else 1.0
		var wing := [[0.47, 0.36], [0.5 - 0.40 * big, 0.10], [0.5 - 0.46 * big, 0.42], [0.5 - 0.30 * big, 0.36], [0.5 - 0.36 * big, 0.60], [0.44, 0.46]]
		_poly(wing, dark)
		_poly(_mirror(wing), dark)
	# 後ろ髪
	var back_hair_len := 0.66 if shape == "queen" else 0.44
	_poly([[0.37, 0.13], [0.63, 0.13], [0.69, back_hair_len], [0.31, back_hair_len]], hair_col.darkened(0.15))
	# 下半身
	if shape == "lamia":
		_line([[0.5, 0.66], [0.66, 0.78], [0.80, 0.90], [0.60, 0.98], [0.32, 0.95], [0.14, 0.86], [0.10, 0.74]], body_col, 0.17)
		_line([[0.5, 0.66], [0.66, 0.78], [0.80, 0.90], [0.60, 0.98], [0.32, 0.95], [0.14, 0.86], [0.10, 0.74]], body_col.lightened(0.35), 0.05)
	else:
		_line([[0.45, 0.70], [0.43, 0.99]], skin, 0.07)
		_line([[0.55, 0.70], [0.57, 0.99]], skin, 0.07)
	# 尻尾
	if shape == "succubus":
		_line([[0.58, 0.68], [0.74, 0.76], [0.86, 0.70], [0.88, 0.58]], dark, 0.018)
		_poly([[0.88, 0.53], [0.85, 0.59], [0.91, 0.59]], dark)
	# 胴と腕
	_line([[0.40, 0.33], [0.31, 0.49], [0.37, 0.62]], skin, 0.05)
	_line([[0.60, 0.33], [0.69, 0.49], [0.63, 0.62]], skin, 0.05)
	_poly([[0.41, 0.30], [0.59, 0.30], [0.64, 0.41], [0.60, 0.53], [0.66, 0.71], [0.34, 0.71], [0.40, 0.53], [0.36, 0.41]], skin)
	# 衣装
	_poly([[0.36, 0.37], [0.64, 0.37], [0.63, 0.45], [0.50, 0.47], [0.37, 0.45]], body_col)
	if shape != "lamia":
		_poly([[0.38, 0.61], [0.62, 0.61], [0.67, 0.72], [0.33, 0.72]], body_col)
	# 首と頭
	_line([[0.5, 0.26], [0.5, 0.32]], skin, 0.05)
	draw_circle(_p(0.5, 0.20), size.x * 0.085, skin)
	# 目と口
	var eye := body_col.lightened(0.2)
	draw_circle(_p(0.468, 0.205), size.x * 0.011, eye)
	draw_circle(_p(0.532, 0.205), size.x * 0.011, eye)
	draw_arc(_p(0.5, 0.228), size.x * 0.018, 0.3, PI - 0.3, 8, body_col.darkened(0.2), 2.0, true)
	# 前髪
	_poly([[0.40, 0.17], [0.44, 0.11], [0.56, 0.11], [0.60, 0.17], [0.61, 0.25], [0.56, 0.18], [0.50, 0.21], [0.44, 0.18], [0.39, 0.25]], hair_col)
	# 角
	if shape == "succubus" or shape == "queen":
		var horn := [[0.43, 0.13], [0.39, 0.03], [0.46, 0.11]]
		_poly(horn, dark.darkened(0.3))
		_poly(_mirror(horn), dark.darkened(0.3))
	# 冠
	if shape == "queen":
		_poly([[0.44, 0.115], [0.45, 0.07], [0.475, 0.10], [0.5, 0.055], [0.525, 0.10], [0.55, 0.07], [0.56, 0.115]], UIKit.GOLD)
	# 仮の絵の印
	draw_string(UIKit.font_bold, Vector2(8, size.y - 10), "仮の絵", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color(1, 1, 1, 0.35))
