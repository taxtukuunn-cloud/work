extends Node
## 遊びの進み具合・設定・回想の開放・操作の割り当てを持つ。

const SAVE_PATH := "user://save.cfg"
const INTENSITY_NAMES := ["あまあま", "ふつう", "はげしい"]
const INTENSITY_MULT := [0.75, 1.0, 1.3]
const TEXT_SPEED_NAMES := ["ゆっくり", "ふつう", "はやい", "一瞬"]
const TEXT_SPEED_CPS := [25.0, 50.0, 100.0, 0.0]

var settings := {"intensity": 1, "text_speed": 1, "unlock_all": false, "volume": 8, "music_volume": 6, "swap_ab": false}
var tutorial_done := false
var unlocked: Dictionary = {}
var lose_count: Dictionary = {}

# 今回の挑戦（保存して「つづきから」で戻れる。桜井 #248 / #116）
var deck: Array = []
var stage := 0
var max_reached := 0  # たどり着いたいちばん先の相手（相手を選ぶ、に使う）
var _lock_until := 0

## 最後に触ったのがコントローラーなら true。操作の案内の表示を切り替える。
signal input_mode_changed(joy: bool)
var joy_mode := false
const HINTS := {
	"accept": ["Enter", "Ⓐ"], "cancel": ["Esc", "Ⓑ"], "end_turn": ["E", "Ⓨ"],
	"surrender": ["Q", "Back"], "skip": ["Ctrl", "RB"], "deck": ["D", "Ⓧ"],
	"move": ["←→", "十字キー"], "updown": ["↑↓", "十字キー"],
}


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	if "--no-save" not in OS.get_cmdline_user_args():
		load_save()
	_setup_input()
	for a in OS.get_cmdline_user_args():
		if a.begins_with("--autoshot="):
			var shot = load("res://tools/autoshot.gd").new()
			shot.out_dir = a.substr("--autoshot=".length())
			add_child.call_deferred(shot)


func hint(key: String) -> String:
	if bool(settings["swap_ab"]) and joy_mode:
		if key == "accept":
			return "Ⓑ"
		if key == "cancel":
			return "Ⓐ"
	return HINTS.get(key, ["", ""])[1 if joy_mode else 0]


func _input(event: InputEvent) -> void:
	var joy := joy_mode
	if event is InputEventJoypadButton:
		joy = true
	elif event is InputEventJoypadMotion and absf(event.axis_value) > 0.5:
		joy = true
	elif event is InputEventKey or event is InputEventMouseButton:
		joy = false
	if joy != joy_mode:
		joy_mode = joy
		input_mode_changed.emit(joy)
	# 開発用：F5 で data/*.json を読み直す（桜井 #046 即時反映）
	if OS.is_debug_build() and event is InputEventKey and event.pressed and event.keycode == KEY_F5:
		DB.load_all()
		print("データを読み直した")


# ---------------------------------------------------------------- 操作の割り当て

func _setup_input() -> void:
	_add_action("end_turn", [KEY_E], [JOY_BUTTON_Y])
	_add_action("surrender", [KEY_Q], [JOY_BUTTON_BACK])
	_add_action("skip", [KEY_CTRL], [JOY_BUTTON_RIGHT_SHOULDER])
	_add_action("deck_view", [KEY_D], [JOY_BUTTON_X])
	_add_axis("ui_left", JOY_AXIS_LEFT_X, -1.0)
	_add_axis("ui_right", JOY_AXIS_LEFT_X, 1.0)
	_add_axis("ui_up", JOY_AXIS_LEFT_Y, -1.0)
	_add_axis("ui_down", JOY_AXIS_LEFT_Y, 1.0)
	apply_button_layout()


## 決定とキャンセルのボタンを入れ替える（桜井 #195）
func apply_button_layout() -> void:
	var a := JOY_BUTTON_B if bool(settings["swap_ab"]) else JOY_BUTTON_A
	var b := JOY_BUTTON_A if bool(settings["swap_ab"]) else JOY_BUTTON_B
	for action in ["ui_accept", "ui_cancel"]:
		for ev in InputMap.action_get_events(action):
			if ev is InputEventJoypadButton and (ev.button_index == JOY_BUTTON_A or ev.button_index == JOY_BUTTON_B):
				InputMap.action_erase_event(action, ev)
	_add_buttons("ui_accept", [a])
	_add_buttons("ui_cancel", [b])


func _add_action(action: String, keys: Array, buttons: Array) -> void:
	if not InputMap.has_action(action):
		InputMap.add_action(action)
	for k in keys:
		var e := InputEventKey.new()
		e.physical_keycode = k
		InputMap.action_add_event(action, e)
	_add_buttons(action, buttons)


func _add_buttons(action: String, buttons: Array) -> void:
	for btn in buttons:
		var j := InputEventJoypadButton.new()
		j.button_index = btn
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
	save()


func has_run() -> bool:
	return deck.size() > 0 and stage < DB.enemies.size()


func advance_stage() -> void:
	stage += 1
	max_reached = maxi(max_reached, mini(stage, DB.enemies.size() - 1))
	if stage >= DB.enemies.size():
		deck = []
	save()


## 画面を切り替えた直後の入力を止める（連打が次の画面に流れないように）
func lock_input(sec: float = 0.25) -> void:
	_lock_until = Time.get_ticks_msec() + int(sec * 1000.0)
	get_viewport().gui_disable_input = true
	get_tree().create_timer(sec).timeout.connect(func(): get_viewport().gui_disable_input = false)


func input_locked() -> bool:
	return Time.get_ticks_msec() < _lock_until


func intensity_mult() -> float:
	return INTENSITY_MULT[int(settings["intensity"])]


func text_cps() -> float:
	return TEXT_SPEED_CPS[int(settings["text_speed"])]


## 報酬でレアが出る確率（はげしいほど高い。桜井 #041 悪魔の窯）
func rare_chance() -> float:
	return float(DB.params["【報酬でレアが出る確率（あまあま・ふつう・はげしい）】"][int(settings["intensity"])])


## 1回目の敗北は lose1、2回目以降は続きの lose2。
func lose_scene_for(enemy_id: String) -> String:
	var n := int(lose_count.get(enemy_id, 0))
	return enemy_id + ("_lose1" if n == 0 else "_lose2")


func register_loss(enemy_id: String) -> void:
	lose_count[enemy_id] = int(lose_count.get(enemy_id, 0)) + 1
	save()


## 新しく開放したら true
func unlock(scene_id: String) -> bool:
	if unlocked.has(scene_id):
		return false
	unlocked[scene_id] = true
	save()
	return true


func is_unlocked(scene_id: String) -> bool:
	return bool(settings["unlock_all"]) or unlocked.has(scene_id)


func gallery_count() -> Vector2i:
	var seen := 0
	var total := 0
	for e in DB.enemies:
		for k in ["_lose1", "_lose2", "_win"]:
			total += 1
			if is_unlocked(e["id"] + k):
				seen += 1
	return Vector2i(seen, total)


# ---------------------------------------------------------------- 保存

func load_save() -> void:
	var cf := ConfigFile.new()
	if cf.load(SAVE_PATH) != OK:
		return
	for k in settings.keys():
		settings[k] = cf.get_value("settings", k, settings[k])
	unlocked = cf.get_value("progress", "unlocked", {})
	lose_count = cf.get_value("progress", "lose_count", {})
	tutorial_done = cf.get_value("progress", "tutorial_done", false)
	deck = cf.get_value("run", "deck", [])
	stage = cf.get_value("run", "stage", 0)
	max_reached = cf.get_value("run", "max_reached", 0)


func save() -> void:
	if "--no-save" in OS.get_cmdline_user_args():
		return
	var cf := ConfigFile.new()
	for k in settings:
		cf.set_value("settings", k, settings[k])
	cf.set_value("progress", "unlocked", unlocked)
	cf.set_value("progress", "lose_count", lose_count)
	cf.set_value("progress", "tutorial_done", tutorial_done)
	cf.set_value("run", "deck", deck)
	cf.set_value("run", "stage", stage)
	cf.set_value("run", "max_reached", max_reached)
	cf.save(SAVE_PATH)
