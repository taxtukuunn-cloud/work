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
var _stop := 0.0  # ヒットストップの残り秒。この間は呼吸を止める
var _hurt := 0.0  # 痛がる顔の残り秒
var _hit_seq := 0

## 余裕の割合で表情を変える（0=笑み / 1=頬を赤らめる / 2=口が開く）
var mood := 0


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
## stop_frames の間は呼吸を止め、体を傾けて押し出し、痛がる顔にする（#003 / #140）
func hit(strength: float = 1.0, stop_frames: float = 0.0) -> void:
	_shake = clampf(strength, 0.3, 1.8)
	_punch = clampf(strength, 0.4, 1.6)
	_flash = 1.0
	_stop = stop_frames / 60.0
	_hurt = maxf(_hurt, stop_frames / 60.0 + 0.12)
	_hit_seq += 1


func set_hp_ratio(r: float) -> void:
	mood = 0 if r > 0.5 else (1 if r > 0.25 else 2)


func _process(delta: float) -> void:
	if _stop > 0.0:
		_stop -= delta
	else:
		_t += delta
		_punch = maxf(0.0, _punch - delta * 5.0)
	_shake = maxf(0.0, _shake - delta * 3.5)
	_hurt = maxf(0.0, _hurt - delta)
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
	var v := Vector2((c.x + (x - c.x) * s), (c.y + (y - c.y) * s))
	# 当たった瞬間は足元を軸に体を傾け、横に押し出す
	if _punch > 0.0:
		var dir := 1.0 if _hit_seq % 2 == 0 else -1.0
		var ang := deg_to_rad(8.0) * _punch * dir
		var pivot := Vector2(0.5, 0.98)
		v = pivot + (v - pivot).rotated(ang) + Vector2(0.06 * _punch * dir, 0)
	return Vector2(v.x * size.x, v.y * size.y) + _off()


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
	# 顔（桜井 #164 フェイシャル）
	var eye := body_col.lightened(0.2)
	var line := body_col.darkened(0.35)
	var w := size.x * 0.006
	if mood >= 1 or _hurt > 0.0:
		var blush := Color(1.0, 0.45, 0.55, 0.55 if mood >= 2 else 0.4)
		draw_circle(_p(0.452, 0.225), size.x * 0.018, blush)
		draw_circle(_p(0.548, 0.225), size.x * 0.018, blush)
	if _hurt > 0.0:
		# ＞＜ の目と、開いた口
		for sx in [0.468, 0.532]:
			var d := 1.0 if sx < 0.5 else -1.0
			draw_polyline(PackedVector2Array([_p(sx - 0.014 * d, 0.197), _p(sx + 0.008 * d, 0.205), _p(sx - 0.014 * d, 0.213)]), line, w * 1.4, true)
		draw_circle(_p(0.5, 0.236), size.x * 0.012, line)
	else:
		draw_circle(_p(0.468, 0.205), size.x * 0.011, eye)
		draw_circle(_p(0.532, 0.205), size.x * 0.011, eye)
		if mood >= 1:
			# 下がった眉
			draw_line(_p(0.455, 0.183), _p(0.48, 0.188), line, w, true)
			draw_line(_p(0.545, 0.183), _p(0.52, 0.188), line, w, true)
		if mood >= 2:
			draw_circle(_p(0.5, 0.234), size.x * 0.010, line)
			# 汗
			_poly([[0.585, 0.165], [0.578, 0.185], [0.592, 0.185]], Color(0.75, 0.9, 1.0, 0.9))
		else:
			draw_arc(_p(0.5, 0.228), size.x * 0.018, 0.3, PI - 0.3, 8, line, 2.0, true)
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
