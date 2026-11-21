class_name Bot
extends RefCounted
## 自動で遊ぶ係。勝率の確認と、壊れていないかの確認に使う。

## 1ターン分を遊ぶ（使えるカードを点数の高い順に使い、最後にターン終了）
static func play_turn(b: Battle) -> void:
	for _i in 20:
		var best := -1
		var best_score := 0.0
		for i in b.hand.size():
			if not b.can_play(i):
				continue
			var s := score(b, b.card_def(b.hand[i]))
			if s > best_score:
				best_score = s
				best = i
		if best < 0:
			break
		b.play(best)
		if b.result != "":
			return
	b.end_turn()


static func score(b: Battle, d: Dictionary) -> float:
	var need := b.incoming_arousal()
	var danger := b.arousal + need >= Battle.CLIMAX_AT
	var s := 0.0
	var self_arousal := 0
	for eff in d.get("effects", []):
		var val := int(eff.get("val", 0))
		match eff.get("op", ""):
			"damage":
				s += 6.0 + val * int(eff.get("hits", 1)) * 0.8
				if val * int(eff.get("hits", 1)) >= b.e_hp:
					s += 50.0
			"block":
				# 来る興奮より多い忍耐は無駄
				s += (8.0 + min(val, need) * 0.8) if need > 0 else 0.0
				if danger and need > 0:
					s += 12.0
			"calm":
				s += (6.0 + val * 0.4) if b.arousal >= 35 else 0.5
				if danger:
					s += 14.0
			"draw":
				s += 7.0 * val
			"energy":
				s += 5.0 * val
			"arousal":
				self_arousal += val
			"cleanse":
				var lewd := 0
				for c in b.hand:
					if c["id"] in Battle.LEWD_CARDS:
						lewd += 1
				s += 8.0 * lewd + 0.5
			"status":
				s += 9.0
			"clear_status":
				s += 6.0 if b.p_status.has("sensitive") else 0.0
			"enemy_status":
				s += 7.0
	if self_arousal > 0:
		if b.arousal + self_arousal + need >= 85:
			return -1.0
		s -= self_arousal * 0.3
	return s / max(1.0, float(d.get("cost", 0)) + 0.5)


## 1戦を最後まで遊ばせて結果を返す
static func run_battle(cards: Dictionary, enemy: Dictionary, deck: Array, mult: float, seed_value: int) -> Dictionary:
	var b := Battle.new()
	b.setup(cards, enemy, deck, mult, seed_value)
	var guard := 0
	while b.result == "" and guard < 60:
		play_turn(b)
		b.take_events()
		guard += 1
	return {"result": b.result if b.result != "" else "timeout", "turns": b.turn, "climaxes": b.climaxes, "hp_left": b.e_hp}
