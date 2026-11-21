extends Node
## data/*.json を読み込んで持っておく。

var cards: Dictionary = {}
var enemies: Array = []
var scenes: Dictionary = {}
var starter_deck: Array = []


func _ready() -> void:
	load_all()


func load_all() -> void:
	cards.clear()
	for c in _read("res://data/cards.json"):
		cards[c["id"]] = c
	enemies = _read("res://data/enemies.json")
	scenes = _read("res://data/scenes.json")
	starter_deck = _read("res://data/starter_deck.json")


func _read(path: String) -> Variant:
	var f := FileAccess.open(path, FileAccess.READ)
	if f == null:
		push_error("読めない: " + path)
		return null
	var data = JSON.parse_string(f.get_as_text())
	if data == null:
		push_error("JSON が壊れている: " + path)
	return data


func enemy(id: String) -> Dictionary:
	for e in enemies:
		if e["id"] == id:
			return e
	return {}


func reward_pool() -> Array:
	var out := []
	for id in cards:
		var r: String = cards[id].get("rarity", "")
		if r == "common" or r == "rare":
			out.append(id)
	return out
