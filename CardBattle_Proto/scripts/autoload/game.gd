extends Node
## 遊びの進み具合・設定・回想の開放を持つ。

const SAVE_PATH := "user://save.cfg"
const INTENSITY_NAMES := ["あまあま", "ふつう", "はげしい"]
const INTENSITY_MULT := [0.75, 1.0, 1.3]
const TEXT_SPEED_NAMES := ["ゆっくり", "ふつう", "はやい", "一瞬"]
const TEXT_SPEED_CPS := [25.0, 50.0, 100.0, 0.0]

var settings := {"intensity": 1, "text_speed": 1, "unlock_all": false}
var unlocked: Dictionary = {}
var lose_count: Dictionary = {}

# 今回の挑戦
var deck: Array = []
var stage := 0


func _ready() -> void:
	_setup_input()
	if "--no-save" not in OS.get_cmdline_user_args():
		load_save()
	for a in OS.get_cmdline_user_args():
		if a.begins_with("--autoshot="):
			var shot = load("res://tools/autoshot.gd").new()
			shot.out_dir = a.substr("--autoshot=".length())
			add_child.call_deferred(shot)


# ---------------------------------------------------------------- 操作の割り当て

func _setup_input() -> void:
	_add_buttons("ui_accept", [JOY_BUTTON_A])
	_add_buttons("ui_cancel", [JOY_BUTTON_B])
	_add_action("end_turn", [KEY_E], [JOY_BUTTON_Y])
	_add_action("surrender", [KEY_Q], [JOY_BUTTON_BACK])
	_add_action("skip", [KEY_CTRL], [JOY_BUTTON_RIGHT_SHOULDER])
	_add_action("deck_view", [KEY_D], [JOY_BUTTON_X])
	_add_axis("ui_left", JOY_AXIS_LEFT_X, -1.0)
	_add_axis("ui_right", JOY_AXIS_LEFT_X, 1.0)
	_add_axis("ui_up", JOY_AXIS_LEFT_Y, -1.0)
	_add_axis("ui_down", JOY_AXIS_LEFT_Y, 1.0)


func _add_action(action: String, keys: Array, buttons: Array) -> void:
	if not InputMap.has_action(action):
		InputMap.add_action(action)
	for k in keys:
		var e := InputEventKey.new()
		e.physical_keycode = k
		InputMap.action_add_event(action, e)
	_add_buttons(action, buttons)


func _add_buttons(action: String, buttons: Array) -> void:
	for b in buttons:
		var j := InputEventJoypadButton.new()
		j.button_index = b
		if not InputMap.action_has_event(action, j):
			InputMap.action_add_event(action, j)


func _add_axis(action: String, axis: int, value: float) -> void:
	var m := InputEventJoypadMotion.new()
	m.axis = axis
	m.axis_value = value
	if not InputMap.action_has_event(action, m):
		InputMap.action_add_event(action, m)


# ---------------------------------------------------------------- 挑戦

func new_run() -> void:
	deck = DB.starter_deck.duplicate()
	stage = 0


func intensity_mult() -> float:
	return INTENSITY_MULT[int(settings["intensity"])]


func text_cps() -> float:
	return TEXT_SPEED_CPS[int(settings["text_speed"])]


## 1回目の敗北は lose1、2回目以降は続きの lose2。
func lose_scene_for(enemy_id: String) -> String:
	var n := int(lose_count.get(enemy_id, 0))
	return enemy_id + ("_lose1" if n == 0 else "_lose2")


func register_loss(enemy_id: String) -> void:
	lose_count[enemy_id] = int(lose_count.get(enemy_id, 0)) + 1
	save()


func unlock(scene_id: String) -> void:
	unlocked[scene_id] = true
	save()


func is_unlocked(scene_id: String) -> bool:
	return bool(settings["unlock_all"]) or unlocked.has(scene_id)


# ---------------------------------------------------------------- 保存

func load_save() -> void:
	var cf := ConfigFile.new()
	if cf.load(SAVE_PATH) != OK:
		return
	for k in settings.keys():
		settings[k] = cf.get_value("settings", k, settings[k])
	unlocked = cf.get_value("progress", "unlocked", {})
	lose_count = cf.get_value("progress", "lose_count", {})


func save() -> void:
	if "--no-save" in OS.get_cmdline_user_args():
		return
	var cf := ConfigFile.new()
	for k in settings:
		cf.set_value("settings", k, settings[k])
	cf.set_value("progress", "unlocked", unlocked)
	cf.set_value("progress", "lose_count", lose_count)
	cf.save(SAVE_PATH)
