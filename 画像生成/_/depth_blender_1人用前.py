# -*- coding: utf-8 -*-
"""構図の下書き（奥行き版・3D 人体）を Blender＋MPFB で書き出す（2026-09-29）
Blender の中で動かす：
  blender.exe --background --factory-startup --python depth_blender.py -- [下書きid,下書きid,...]
- 関節の座標は 構図下書き\\_関節.json（pose_templates.py の骨格の下書きから作ったもの）
- MPFB で成人の人体を作る：主人公＝男性・細身・筋肉少なめ・身長160cm／相手＝女性・身長175cm
- 胴の向きは FRONT（胸が向く方向）で決め、腕・脚・首は骨格の下書きの関節の方向へ向ける
- 出力：構図下書き\\depth3d_<id>.png（手前ほど白・背景は黒）"""
import bpy, json, math, os, sys
from mathutils import Matrix, Vector
from bl_ext.user_default.mpfb.services.humanservice import HumanService
from bl_ext.user_default.mpfb.services.targetservice import TargetService

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "構図下書き")
J = json.load(open(os.path.join(OUT, "_関節.json"), encoding="utf-8"))
W, H = J["W"], J["H"]
M_PER_PX = 1.60 / J["HERO_H"]       # 主人公の身長 1040px ＝ 1.60m
HEIGHT = {"hero": 1.60, "partner": 1.75}
BODY = {  # MPFB の体つき（0〜1）。age 0.5＝成人
    "hero": {"gender": 1.0, "age": 0.5, "muscle": 0.3, "weight": 0.35, "proportions": 0.6},
    "partner": {"gender": 0.0, "age": 0.5, "muscle": 0.4, "weight": 0.5, "proportions": 0.6, "cupsize": 0.6},
}
# 胸が向く方向（世界座標：x＝画面右、y＝画面の奥、z＝上）。人物の並びは _関節.json と同じ
TOWARD = (0, -1, 0); LEFT = (-1, 0, 0); RIGHT = (1, 0, 0); UP = (0, 0, 1); DOWN = (0, 0, -1)
FRONT = {
    "standing_embrace": [RIGHT, LEFT], "seated_behind": [TOWARD, TOWARD], "lying_leanover": [UP, (-0.4, 0, -1)],
    "all_fours_behind": [DOWN, LEFT], "all_fours_behind_reach": [DOWN, (-0.3, 0, -1)],
    "girl_on_top_kiss": [UP, DOWN], "girl_on_top_straddle": [UP, LEFT], "legs_up_front": [UP, LEFT],
    "standing_foot": [(1, 0, 0.4), LEFT], "side_handjob": [TOWARD, TOWARD], "arms_up_bound": [TOWARD, LEFT],
    "neck_bite": [TOWARD, TOWARD],
    "standing_behind_hug": [TOWARD, TOWARD], "kneel_behind": [TOWARD, TOWARD], "lap_pillow": [UP, RIGHT],
    "standing_front_chest": [RIGHT, LEFT], "seated_front_chest": [RIGHT, LEFT], "kneel_front_chest": [RIGHT, LEFT],
}
LIMBS = [("upperarm_l", "lsho", "lelb"), ("lowerarm_l", "lelb", "lwri"), ("upperarm_r", "rsho", "relb"), ("lowerarm_r", "relb", "rwri"),
         ("thigh_l", "lhip", "lknee"), ("calf_l", "lknee", "lank"), ("thigh_r", "rhip", "rknee"), ("calf_r", "rknee", "rank")]
# 2次元の骨格では表せない向き（正面から見た座り姿：太ももはカメラ側へ）を世界座標で直接決める。{下書き: {人物の番号: {骨: 方向}}}
SEATED = {"thigh_l": (0.12, -1, -0.12), "thigh_r": (-0.12, -1, -0.12), "calf_l": (0.05, -0.15, -1), "calf_r": (-0.05, -0.15, -1)}
# 後ろから抱く人の腕：上腕は前（カメラ側）へ、前腕は胸の中央へ回す
HUG_FRONT = {"upperarm_r": (0.25, -1, -0.45), "lowerarm_r": (1, -0.35, -0.1), "upperarm_l": (-0.25, -1, -0.45), "lowerarm_l": (-1, -0.35, -0.1)}
KNEEL_UP = {"thigh_l": (0.03, 0, -1), "thigh_r": (-0.03, 0, -1), "calf_l": (0.02, 1, -0.05), "calf_r": (-0.02, 1, -0.05)}   # 膝立ち：すねは後ろへ
OVERRIDE = {"seated_behind": {0: SEATED}, "side_handjob": {0: SEATED, 1: SEATED}, "kneel_behind": {0: KNEEL_UP, 1: HUG_FRONT}, "standing_behind_hug": {1: HUG_FRONT}}
CUR = {"pid": "", "i": 0}
# 後ろにいる人物を奥へずらす（m）。{下書き: {人物の番号: 奥行き}}
DEPTH_OFFSET = {"seated_behind": {1: 0.45}, "neck_bite": {1: 0.18}, "standing_behind_hug": {1: 0.22}, "kneel_behind": {1: 0.35}}


def front_of(pid, i):
    base = pid[:-2] if pid.endswith("_r") else pid
    f = Vector(FRONT[base][i])
    if pid.endswith("_r"):
        f.x = -f.x
    return f


def to_world(p, scale):
    """下書きの座標（px）→ 世界座標（m）。画面の中心が原点、上が +z"""
    return Vector(((p[0] - W / 2) * M_PER_PX, 0.0, (H - p[1]) * M_PER_PX))


def mid(kp, a, b):
    return [(kp[a][0] + kp[b][0]) / 2, (kp[a][1] + kp[b][1]) / 2]


def make_person(role, scale):
    macro = TargetService.get_default_macro_info_dict()
    macro.update(BODY[role])
    mesh = HumanService.create_human(macro_detail_dict=macro)
    rig = HumanService.add_builtin_rig(mesh, "game_engine")
    bpy.context.view_layer.update()
    zs = [(mesh.matrix_world @ v.co).z for v in mesh.data.vertices]
    k = HEIGHT[role] * scale / (max(zs) - min(zs))
    return mesh, rig, k


def aim(rig, bone, target_dir):
    """pose bone を、世界座標の target_dir の方向へ向ける（根元の位置は保つ）"""
    bpy.context.view_layer.update()
    pb = rig.pose.bones[bone]
    mw = rig.matrix_world
    head = mw @ pb.head; tail = mw @ pb.tail
    cur = (tail - head).normalized()
    if target_dir.length < 1e-6:
        return
    q = cur.rotation_difference(target_dir.normalized())
    rot_arm = (mw.to_3x3().normalized().inverted() @ q.to_matrix() @ mw.to_3x3().normalized())
    hd = pb.head.copy()
    pb.matrix = Matrix.Translation(hd) @ rot_arm.to_4x4() @ Matrix.Translation(-hd) @ pb.matrix


def pose_person(rig, kp, front, k, scale, role="hero"):
    neck = to_world(kp["neck"], scale)
    if "rhip" in kp and "lhip" in kp:
        hip = to_world(mid(kp, "rhip", "lhip"), scale)
    else:   # 腰から下を省いた人物（後ろに立つ人など）：首から真下に胴の長さ（頭2.55個分）
        hip = neck - Vector((0, 0, HEIGHT[role] * scale / 7.3 * 2.55))
    up = (neck - hip).normalized()
    f = Vector(front).normalized()
    f = (f - f.dot(up) * up).normalized()
    left = up.cross(f)
    R = Matrix((left, f, up)).transposed()                  # 目標の向き
    R0 = Matrix(((1, 0, 0), (0, -1, 0), (0, 0, 1))).transposed()   # MPFB の初期（左=+x・前=-y・上=+z）
    rot = (R @ R0.inverted()).to_4x4()
    rig.matrix_world = rot @ Matrix.Scale(k, 4)
    bpy.context.view_layer.update()
    pel = rig.matrix_world @ rig.pose.bones["pelvis"].head
    rig.matrix_world = Matrix.Translation(hip - pel) @ rig.matrix_world
    ov = OVERRIDE.get(CUR["pid"], {}).get(CUR["i"], {})
    for bone, a, b in LIMBS:
        if bone in ov:
            aim(rig, bone, Vector(ov[bone]))
        elif a in kp and b in kp:
            aim(rig, bone, to_world(kp[b], scale) - to_world(kp[a], scale))
    head_pts = [kp[n] for n in ("nose", "reye", "leye") if n in kp]
    if head_pts:
        hx = sum(p[0] for p in head_pts) / len(head_pts); hy = sum(p[1] for p in head_pts) / len(head_pts)
        aim(rig, "neck_01", to_world([hx, hy], scale) - neck)


def depth_material():
    m = bpy.data.materials.new("depth"); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    mr = nt.nodes.new("ShaderNodeMapRange"); mr.name = "range"
    em = nt.nodes.new("ShaderNodeEmission"); out = nt.nodes.new("ShaderNodeOutputMaterial")
    nt.links.new(geo.outputs["Position"], sep.inputs[0])
    nt.links.new(sep.outputs["Y"], mr.inputs["Value"])      # 奥行き＝世界の y（カメラは -y 側から +y を見る）
    mr.inputs["To Min"].default_value = 1.0; mr.inputs["To Max"].default_value = 0.05   # 手前ほど白
    nt.links.new(mr.outputs["Result"], em.inputs["Color"])
    nt.links.new(em.outputs["Emission"], out.inputs["Surface"])
    return m


def render(pid, path):
    t = J["templates"][pid]; scale = t["scale"]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    meshes = []
    for i, p in enumerate(t["people"]):
        mesh, rig, k = make_person(p["role"], scale)
        CUR["pid"], CUR["i"] = pid, i
        pose_person(rig, p["kp"], front_of(pid, i), k, scale, p["role"])
        dy = DEPTH_OFFSET.get(pid[:-2] if pid.endswith("_r") else pid, {}).get(i, 0.0)
        if dy:
            rig.matrix_world = Matrix.Translation((0, dy, 0)) @ rig.matrix_world
        # 奥の人物は少し奥へ（重なりの前後関係。後ろに立つ構図など）
        meshes.append(mesh)
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ys = []
    for m in meshes:
        ev = m.evaluated_get(dg); me = ev.to_mesh()
        ys += [(ev.matrix_world @ v.co).y for v in me.vertices]; ev.to_mesh_clear()
    mat = depth_material()
    mat.node_tree.nodes["range"].inputs["From Min"].default_value = min(ys)
    mat.node_tree.nodes["range"].inputs["From Max"].default_value = max(ys) + 1e-3
    for m in meshes:
        m.data.materials.clear(); m.data.materials.append(mat)
        for s in m.material_slots:
            s.material = mat
    cam_data = bpy.data.cameras.new("cam"); cam_data.type = "ORTHO"
    cam_data.sensor_fit = "VERTICAL"; cam_data.ortho_scale = H * M_PER_PX
    cam = bpy.data.objects.new("cam", cam_data); bpy.context.scene.collection.objects.link(cam)
    cam.location = (0, -20, H / 2 * M_PER_PX); cam.rotation_euler = (math.radians(90), 0, 0)
    sc = bpy.context.scene; sc.camera = cam
    sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 4
    sc.render.resolution_x, sc.render.resolution_y = W, H
    sc.render.film_transparent = False
    if sc.world is None:
        sc.world = bpy.data.worlds.new("w")
    sc.world.use_nodes = False; sc.world.color = (0, 0, 0)
    sc.view_settings.view_transform = "Raw"
    sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_mode = "RGB"
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)


def main():
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ids = args[0].split(",") if args else list(J["templates"])
    for pid in ids:
        path = os.path.join(OUT, "depth3d_%s.png" % pid)
        render(pid, path)
        print("書き出し:", pid, flush=True)


main()
