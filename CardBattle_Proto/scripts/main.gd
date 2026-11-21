extends Control
## 画面の切り替えと、遊びの流れ（会話 → 戦闘 → シーン → 報酬 → 次の相手）を受け持つ。

var current: Control
var rng := RandomNumberGenerator.new()
var toast_layer: CanvasLayer
var _pending_toast := ""


func _ready() -> void:
	theme = UIKit.build_theme()
	rng.randomize()
	toast_layer = CanvasLayer.new()
	toast_layer.layer = 10
	add_child(toast_layer)
	# カーソルが動いたら小さく鳴らす（桜井 #104 ノーリアクションを排除）
	get_viewport().gui_focus_changed.connect(func(_c): Sfx.play("move"))
	show_title()


## 画面の切り替えは素早く（桜井 #244）
func _swap(node: Control) -> void:
	if current:
		current.queue_free()
	current = node
	Game.lock_input(0.25)
	node.modulate.a = 0.0
	add_child(node)
	move_child(node, 0)
	create_tween().tween_property(node, "modulate:a", 1.0, 0.12)
	if _pending_toast != "":
		toast(_pending_toast)
		_pending_toast = ""


## 画面の右上に短く知らせる（桜井 #095 ほめる・#023 目の前の目標）
func toast(text: String) -> void:
	Sfx.play("unlock")
	var p := PanelContainer.new()
	p.add_theme_stylebox_override("panel", UIKit.box(Color(0.15, 0.08, 0.18, 0.95), UIKit.GOLD, 10, 2, 14))
	p.add_child(UIKit.label(text, 18, UIKit.GOLD, true))
	toast_layer.add_child(p)
	p.position = Vector2(640 - p.get_combined_minimum_size().x / 2.0, -80)
	var tw := p.create_tween()
	tw.tween_property(p, "position:y", 8.0, 0.2).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
	tw.tween_interval(2.2)
	tw.tween_property(p, "modulate:a", 0.0, 0.3)
	tw.tween_callback(p.queue_free)


# ---------------------------------------------------------------- 画面

func show_title() -> void:
	Sfx.music("title")
	_swap(Menus.title(_start_run, show_gallery, show_settings, func(): get_tree().quit(), _next_stage, show_select))


func show_select() -> void:
	_swap(Menus.select_enemy(func(i):
		if Game.deck.is_empty():
			Game.deck = DB.starter_deck.duplicate()
		Game.stage = i
		Game.save()
		_start_battle(), show_title))


func show_gallery() -> void:
	_swap(Menus.gallery(func(sid): play_scene(sid, show_gallery), show_title))


func show_settings() -> void:
	_swap(Menus.settings(show_title))


func play_scene(id: String, on_done: Callable) -> void:
	var s := SceneScreen.new().setup(id)
	s.finished.connect(on_done, CONNECT_ONE_SHOT)
	_swap(s)


# ---------------------------------------------------------------- 遊びの流れ

func _enemy() -> Dictionary:
	return DB.enemies[Game.stage]


func _start_run() -> void:
	Game.new_run()
	_next_stage()


func _next_stage() -> void:
	play_scene(_enemy()["id"] + "_intro", _start_battle)


func _start_battle() -> void:
	var b := BattleScreen.new().setup(_enemy(), Game.deck)
	b.finished.connect(_on_battle_end, CONNECT_ONE_SHOT)
	_swap(b)


func _unlock(sid: String) -> void:
	if Game.unlock(sid):
		var gc := Game.gallery_count()
		_pending_toast = "回想に追加：%s（%d / %d）" % [DB.scenes[sid]["title"], gc.x, gc.y]


var _earned_rare := false


func _on_battle_end(result: String) -> void:
	var e := _enemy()
	_earned_rare = (current as BattleScreen).earned_rare if current is BattleScreen else false
	if result == "win":
		var sid: String = e["id"] + "_win"
		play_scene(sid, func():
			_unlock(sid)
			_after_win())
	else:
		var sid := Game.lose_scene_for(e["id"])
		Game.register_loss(e["id"])
		play_scene(sid, func():
			_unlock(sid)
			_show_lose())


func _after_win() -> void:
	Game.advance_stage()
	if Game.stage >= DB.enemies.size():
		play_scene("ending", show_title)
	else:
		_swap(Menus.reward(rng, _on_reward, _earned_rare))


func _on_reward(card_id: String) -> void:
	if card_id != "":
		Game.deck.append(card_id)
		Game.save()
		Sfx.play("confirm")
	_next_stage()


func _show_lose() -> void:
	var e := _enemy()
	_swap(Menus.lose(e["name"], int(Game.lose_count.get(e["id"], 0)), _start_battle, show_title, func():
		Game.settings["intensity"] = maxi(0, int(Game.settings["intensity"]) - 1)
		Game.save()
		_pending_toast = "責めの強さを「%s」にした（設定でいつでも戻せる）" % Game.INTENSITY_NAMES[int(Game.settings["intensity"])]
		_start_battle()))
