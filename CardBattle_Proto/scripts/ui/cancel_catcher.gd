class_name CancelCatcher
extends Node
## 戻るボタン（Esc／Ⓑ）を受けて、決めた処理を呼ぶ（桜井 #104 ノーリアクションを排除）。

var callback: Callable


static func attach(parent: Node, cb: Callable) -> void:
	var c := CancelCatcher.new()
	c.callback = cb
	parent.add_child(c)


func _unhandled_input(event: InputEvent) -> void:
	if Game.input_locked():
		return
	if event.is_action_pressed("ui_cancel"):
		get_viewport().set_input_as_handled()
		Sfx.play("confirm")
		callback.call()
