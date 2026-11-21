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


# ================================================================ 音楽・環境音（桜井 #069 / #202）
# 戦闘は心音のループで、高揚の段階でテンポが上がる。シーンは場所ごとの環境音。

var _music_a: AudioStreamPlayer
var _music_b: AudioStreamPlayer
var _music_name := ""
var _loops: Dictionary = {}


func _music_players() -> void:
	if _music_a:
		return
	_music_a = AudioStreamPlayer.new()
	_music_b = AudioStreamPlayer.new()
	add_child(_music_a)
	add_child(_music_b)


func _music_db() -> float:
	return -12.0 + linear_to_db(maxf(0.001, float(Game.settings.get("music_volume", 6)) / 10.0))


func refresh_music_volume() -> void:
	if _music_a and _music_a.playing:
		_music_a.volume_db = _music_db()


## 名前で音楽を切り替える（同じなら何もしない）。0.4秒で入れ替える。
func music(name: String) -> void:
	_music_players()
	if name == _music_name:
		return
	_music_name = name
	var old := _music_a
	_music_a = _music_b
	_music_b = old
	if old.playing:
		var tw := create_tween()
		tw.tween_property(old, "volume_db", -60.0, 0.4)
		tw.tween_callback(old.stop)
	if name == "":
		return
	if not _loops.has(name):
		_loops[name] = _make_loop(name)
	_music_a.stream = _loops[name]
	_music_a.volume_db = -60.0
	_music_a.play()
	create_tween().tween_property(_music_a, "volume_db", _music_db(), 0.4)


func _make_loop(name: String) -> AudioStreamWAV:
	var s: AudioStreamWAV
	match name:
		"battle_0", "battle_1", "battle_2":
			var bpm: float = [70.0, 95.0, 130.0][int(name.right(1))]
			var beat := 60.0 / bpm
			var length := beat * 8.0
			var root: float = [110.0, 123.47, 130.81][int(name.right(1))]
			s = _make(length, func(t):
				var tb := fmod(t, beat)
				var heart := _heartbeat(tb) * 0.9
				var pad := (sin(TAU * root * t) + sin(TAU * root * 1.5 * t) * 0.6 + sin(TAU * root * 2.0 * t) * 0.3) * 0.07
				pad *= 0.75 + 0.25 * sin(TAU * t / length)
				return heart + pad)
		"title":
			s = _make(8.0, func(t):
				var chord := [220.0, 277.18, 329.63, 415.3]
				var v := 0.0
				for i in chord.size():
					v += sin(TAU * chord[i] * t + i) * (0.5 + 0.5 * sin(TAU * t / 8.0 + i * 1.3))
				return v * 0.06)
		"tavern":
			s = _make(6.0, func(t):
				var murmur := _rand() * (0.08 + 0.05 * sin(TAU * 0.7 * t) * sin(TAU * 1.3 * t))
				var clink := sin(TAU * 2600.0 * t) * exp(-fmod(t, 2.3) * 30.0) * 0.08
				return murmur * 0.6 + clink)
		"swamp":
			s = _make(6.0, func(t):
				var drop := 0.0
				for k in [0.4, 1.7, 2.9, 4.6]:
					var dt: float = t - k
					if dt > 0.0:
						drop += sin(TAU * (900.0 + 1400.0 * exp(-dt * 30.0)) * dt) * exp(-dt * 18.0) * 0.25
				return drop + _rand() * 0.02)
		"castle":
			s = _make(8.0, func(t):
				return (sin(TAU * 55.0 * t) + sin(TAU * 55.7 * t) + sin(TAU * 82.4 * t) * 0.5) * 0.09 + _rand() * 0.01)
		_:
			s = _make(1.0, func(_t): return 0.0)
	s.loop_mode = AudioStreamWAV.LOOP_FORWARD
	s.loop_begin = 0
	s.loop_end = int(s.data.size() / 2)
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
