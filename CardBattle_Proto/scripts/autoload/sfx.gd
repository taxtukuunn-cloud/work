extends Node
## 効果音。素材ファイルを使わず、起動時にプログラムで波形を作る。
## 桜井 #032：音量はプレイヤーへの影響度の順（絶頂 ＞ 大きな一撃 ＞ 一撃 ＞ 責め ＞ 高揚 ＞ …）。
## 桜井 #165：ヒット音はアタック強め、残響ほどほど。

const RATE := 22050
const VOLUME_DB := {
	"climax": 0.0, "win": -2.0, "hit_big": -2.0, "hit": -4.0, "arouse": -6.0, "arouse_big": -4.0,
	"tier_up": -6.0, "block": -9.0, "play": -10.0, "deny": -9.0, "confirm": -11.0,
	"move": -18.0, "page": -20.0, "unlock": -6.0,
}

var streams: Dictionary = {}
var players: Array = []
var _next := 0
var _noise := RandomNumberGenerator.new()


func _ready() -> void:
	_noise.seed = 12345
	for i in 12:
		var p := AudioStreamPlayer.new()
		add_child(p)
		players.append(p)
	streams["move"] = _make(0.03, func(t): return sin(TAU * 1500.0 * t) * exp(-t * 120.0))
	streams["page"] = _make(0.03, func(t): return sin(TAU * 950.0 * t) * exp(-t * 110.0))
	streams["confirm"] = _make(0.09, func(t):
		var f := 880.0 if t < 0.04 else 1320.0
		return sin(TAU * f * t) * exp(-t * 30.0))
	streams["deny"] = _make(0.14, func(t): return (1.0 if sin(TAU * 130.0 * t) > 0.0 else -1.0) * 0.5 * exp(-t * 18.0))
	streams["play"] = _make(0.13, func(t):
		var sweep := sin(TAU * (500.0 + 3000.0 * t) * t) * 0.35
		return (_rand() * 0.6 + sweep) * sin(PI * t / 0.13))
	streams["hit"] = _make(0.16, func(t):
		var crack := _rand() * exp(-t * 90.0)
		var thump := sin(TAU * 150.0 * t) * exp(-t * 28.0)
		return crack * 0.8 + thump)
	streams["hit_big"] = _make(0.28, func(t):
		var crack := _rand() * exp(-t * 50.0)
		var thump := sin(TAU * (110.0 - 60.0 * t) * t) * exp(-t * 14.0)
		return crack * 0.9 + thump)
	streams["block"] = _make(0.12, func(t): return (sin(TAU * 95.0 * t) + _rand() * 0.25) * exp(-t * 35.0))
	streams["arouse"] = _make(0.32, func(t): return _heartbeat(t) * 0.9 + sin(TAU * 2100.0 * t) * 0.06 * exp(-t * 8.0))
	streams["arouse_big"] = _make(0.42, func(t): return _heartbeat(t) + _rand() * 0.15 * exp(-t * 20.0) + sin(TAU * 1800.0 * t) * 0.1 * exp(-t * 6.0))
	streams["tier_up"] = _make(0.22, func(t):
		var notes := [660.0, 880.0, 1320.0]
		var i := mini(int(t / 0.06), 2)
		return sin(TAU * notes[i] * t) * exp(-(t - i * 0.06) * 18.0) * 0.8)
	streams["climax"] = _make(1.1, func(t):
		var burst := _rand() * exp(-t * 12.0) * 0.7
		var fall := sin(TAU * (1300.0 - 900.0 * minf(t, 0.7)) * t) * exp(-t * 3.0) * 0.6
		var chord := (sin(TAU * 523.0 * t) + sin(TAU * 659.0 * t) + sin(TAU * 784.0 * t)) * 0.15 * exp(-t * 2.5)
		return burst + fall + chord)
	streams["win"] = _make(0.6, func(t):
		var notes := [523.0, 659.0, 784.0, 1046.0]
		var i := mini(int(t / 0.08), 3)
		return sin(TAU * notes[i] * t) * exp(-(t - i * 0.08) * 6.0) * 0.7)
	streams["unlock"] = _make(0.35, func(t):
		var notes := [988.0, 1318.0]
		var i := mini(int(t / 0.1), 1)
		return sin(TAU * notes[i] * t) * exp(-(t - i * 0.1) * 9.0) * 0.6)


func _rand() -> float:
	return _noise.randf_range(-1.0, 1.0)


func _heartbeat(t: float) -> float:
	var a := sin(TAU * 70.0 * t) * exp(-t * 30.0)
	var t2 := t - 0.15
	var b := 0.0
	if t2 > 0.0:
		b = sin(TAU * 62.0 * t2) * exp(-t2 * 24.0) * 0.8
	return a + b


func _make(length: float, fn: Callable) -> AudioStreamWAV:
	var n := int(length * RATE)
	var data := PackedByteArray()
	data.resize(n * 2)
	for i in n:
		var v: float = clampf(fn.call(float(i) / RATE), -1.0, 1.0)
		data.encode_s16(i * 2, int(v * 32000.0))
	var s := AudioStreamWAV.new()
	s.format = AudioStreamWAV.FORMAT_16_BITS
	s.mix_rate = RATE
	s.stereo = false
	s.data = data
	return s


func play(name: String, pitch: float = 1.0) -> void:
	if not streams.has(name):
		return
	var p: AudioStreamPlayer = players[_next]
	_next = (_next + 1) % players.size()
	p.stream = streams[name]
	p.volume_db = VOLUME_DB.get(name, -10.0) + linear_to_db(float(Game.settings.get("volume", 8)) / 10.0)
	p.pitch_scale = pitch
	p.play()
