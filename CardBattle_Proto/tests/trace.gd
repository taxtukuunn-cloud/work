extends Node
func _ready():
	var b := Battle.new()
	b.setup(DB.cards, DB.enemies[2], DB.starter_deck + ["heavy", "focus"], 1.0, 5)
	while b.result == "" and b.turn < 25:
		var before_hand := []
		for c in b.hand: before_hand.append(c["id"])
		var a0 := b.arousal
		var plays := []
		var hp0 := b.e_hp
		var intent := b.intent_text()
		# copy of bot loop to log plays
		for _i in 20:
			var best := -1; var bs := 0.0
			for i in b.hand.size():
				if not b.can_play(i): continue
				var s := Bot.score(b, b.card_def(b.hand[i]))
				if s > bs: bs = s; best = i
			if best < 0: break
			plays.append(b.hand[best]["id"])
			b.play(best)
		var blk := b.block
		b.end_turn()
		b.take_events()
		print("T%d 手札%s 使用%s 忍耐%d 予告[%s] 興奮%d→%d 余裕%d→%d" % [b.turn-1, before_hand, plays, blk, intent, a0, b.arousal, hp0, b.e_hp])
	print(b.result)
	get_tree().quit()
