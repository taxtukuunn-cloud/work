class_name HitMark
extends Control
## 当たった位置に一瞬だけ出る星形の印（桜井 #130 ヒットマーク）。
## 黒い縁を敷いてどんな背景でも見えるようにし、短く消す。

var life := 0.0
var max_life := 0.16
var radius := 40.0
var col := Color.WHITE
var spin := 0.0


static func spawn(parent: Control, pos: Vector2, r: float, c: Color) -> HitMark:
	var m := HitMark.new()
	m.position = pos
	m.radius = r
	m.col = c
	m.spin = randf() * TAU
	m.mouse_filter = Control.MOUSE_FILTER_IGNORE
	parent.add_child(m)
	return m


func _process(delta: float) -> void:
	life += delta
	if life >= max_life:
		queue_free()
		return
	queue_redraw()


func _star(r_out: float, r_in: float, points: int) -> PackedVector2Array:
	var arr := PackedVector2Array()
	for i in points * 2:
		var r := r_out if i % 2 == 0 else r_in
		var a := spin + PI * i / points
		arr.append(Vector2(cos(a), sin(a)) * r)
	return arr


func _draw() -> void:
	var k := life / max_life
	var r := radius * (0.7 + 0.5 * k)
	var fade := 1.0 - k * k
	draw_colored_polygon(_star(r * 1.18, r * 0.55, 8), Color(0, 0, 0, 0.85 * fade))
	draw_colored_polygon(_star(r, r * 0.42, 8), Color(col, fade))
	draw_colored_polygon(_star(r * 0.45, r * 0.2, 8), Color(1, 1, 1, fade))
	draw_arc(Vector2.ZERO, r * (0.9 + 0.9 * k), 0.0, TAU, 40, Color(1, 1, 1, 0.7 * fade), 4.0, true)
