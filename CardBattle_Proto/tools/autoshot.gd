extends Node
## 画面確認用。コントローラーの入力を送り込みながら、要所で画面を撮る。
##   xvfb-run godot --path . -- --no-save --autoshot=/出力先

var out_dir := ""
var n := 0


func _ready() -> void:
	DirAccess.make_dir_recursive_absolute(out_dir)
	await _run()
	get_tree().quit()


func wait(t: float) -> void:
	await get_tree().create_timer(t, true, false, true).timeout


func shot(name: String) -> void:
	await RenderingServer.frame_post_draw
	n += 1
	var img := get_viewport().get_texture().get_image()
	img.save_png("%s/%02d_%s.png" % [out_dir, n, name])
	print("撮影: ", name)


## コントローラーのボタンを押して離す
func joy(button: JoyButton, hold: float = 0.05) -> void:
	var e := InputEventJoypadButton.new()
	e.button_index = button
	e.pressed = true
	Input.parse_input_event(e)
	await wait(hold)
	var r := InputEventJoypadButton.new()
	r.button_index = button
	r.pressed = false
	Input.parse_input_event(r)
	await wait(0.08)


## シーンが終わるまで決定を押し続ける
func through_scene(limit: int = 60) -> void:
	await wait(0.35)
	for i in limit:
		if not (main().current is SceneScreen):
			return
		await joy(JOY_BUTTON_A)
		await wait(0.02)


func main() -> Node:
	return get_tree().root.get_node("Main")


func battle() -> BattleScreen:
	return main().current as BattleScreen


## 手札から指定のカードを探してフォーカスし、使う
func use_card(id: String) -> bool:
	var b := battle()
	for i in b.battle.hand.size():
		if b.battle.hand[i]["id"] == id and b.battle.can_play(i):
			(b.hand_box.get_child(i) as Control).grab_focus()
			await wait(0.15)
			await joy(JOY_BUTTON_A)
			return true
	return false


func _run() -> void:
	await wait(0.8)
	await shot("タイトル")
	await joy(JOY_BUTTON_A)  # はじめから
	await wait(0.6)
	await shot("導入の会話")
	await through_scene()
	await wait(0.8)
	await shot("戦闘の開始と案内")
	await joy(JOY_BUTTON_DPAD_RIGHT)
	await wait(0.3)
	await shot("カードを選ぶ")
	# 攻撃を使う瞬間（ヒットストップ中）を撮る
	var b := battle()
	for i in b.battle.hand.size():
		if b.battle.hand[i]["id"] == "strike":
			(b.hand_box.get_child(i) as Control).grab_focus()
	await wait(0.2)
	await joy(JOY_BUTTON_A)
	await wait(0.24)
	await shot("ヒットマーク")
	await wait(1.0)
	await shot("案内が進む")
	await joy(JOY_BUTTON_Y)  # ターン終了
	await wait(0.75)
	await shot("相手の責め")
	await wait(2.5)
	# 高揚を限界寸前にして、カードの「今なら」表示を見る
	b = battle()
	b.battle.arousal = 78
	b._refresh()
	await wait(0.5)
	await shot("限界寸前")
	await joy(JOY_BUTTON_X)
	await wait(0.3)
	await shot("デッキを見る")
	await joy(JOY_BUTTON_B)
	await wait(0.2)
	# 絶頂の演出
	b.battle.arousal = 96
	b._refresh()
	await joy(JOY_BUTTON_Y)
	await wait(1.25)
	await shot("絶頂の演出")
	await wait(2.5)
	# 勝利の演出
	b = battle()
	b.battle.e_hp = 1
	b._refresh()
	await wait(0.3)
	if await use_card("strike") or await use_card("heavy"):
		await wait(1.6)
		await shot("勝利")
		await joy(JOY_BUTTON_A)
	await wait(1.0)
	await shot("見送りのシーン")
	await through_scene()
	await wait(0.5)
	await shot("報酬と回想の知らせ")
	await joy(JOY_BUTTON_DPAD_RIGHT)
	await wait(0.2)
	await joy(JOY_BUTTON_A)
	await through_scene()
	await wait(1.0)
	await shot("2戦目")
	battle().battle.arousal = 45
	battle()._refresh()
	await wait(0.3)
	await joy(JOY_BUTTON_BACK)  # おねだり
	await wait(0.4)
	await shot("おねだりの確認")
	await joy(JOY_BUTTON_DPAD_LEFT)
	await wait(0.2)
	await joy(JOY_BUTTON_A)
	await wait(2.2)
	await shot("敗北シーン")
	await through_scene()
	await wait(0.6)
	await shot("敗北のあと")
	# 2回負けたことにして、救済の選択肢を見る
	Game.lose_count["serpena"] = 2
	main()._show_lose()
	await wait(0.6)
	await shot("救済の選択肢")
	main().show_title()
	await wait(0.6)
	await shot("タイトル（回想の数）")
	main().show_gallery()
	await wait(0.6)
	await shot("回想")
	main().show_settings()
	await wait(0.6)
	await shot("設定")
	Game.max_reached = 2
	Game.deck = DB.starter_deck.duplicate()
	Game.stage = 1
	main().show_title()
	await wait(0.6)
	await shot("タイトル（つづきから）")
	main().show_select()
	await wait(0.6)
	await shot("相手を選ぶ")
	# ボス戦の見た目
	Game.stage = 2
	main()._start_battle()
	await wait(1.0)
	await shot("ボス戦")
