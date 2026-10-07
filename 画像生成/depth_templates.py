# -*- coding: utf-8 -*-
"""構図の下書き（奥行き版・ControlNet Depth 用）を描く（2026-09-29）
骨格の下書き（pose_templates.py）の関節に奥行き（手前・奥）を足し、成人の比率の「人形」（頭・胴・手足を丸い筒で表す）を
立体として並べ、手前ほど白い奥行き画像にする。Blender などは使わない（プログラムで直接描く）。
- 出力：画像生成\\構図下書き\\depth_<id>.png と ComfyUI\\input\\pose_depth_<id>.png
- 使うモデル：xinsir_union_sdxl_promax（union_type=depth）
使い方: python depth_templates.py [--preview]"""
import os, sys, shutil
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pose_templates as PT

W, H = PT.W, PT.H
# 下書きごとの向きと人物の奥行き。side＝横から見た構図（左右の手足で手前・奥が分かれる）、front＝正面
# z は画面の奥行き（小さいほど手前）。person_z は [骨格の並び順] で、役は PT.ROLES
META = {
    "standing_embrace": ("side", [0, 10]), "seated_behind": ("front", [0, 90]), "lying_leanover": ("side", [0, -10]),
    "all_fours_behind": ("side", [0, 10]), "all_fours_behind_reach": ("side", [0, 0]),
    "girl_on_top_kiss": ("side", [0, -5]), "girl_on_top_straddle": ("side", [0, 0]), "legs_up_front": ("side", [0, 0]),
    "standing_foot": ("side", [0, 0]), "side_handjob": ("front", [0, 0]), "arms_up_bound": ("front", [0, 20]),
    "neck_bite": ("front", [0, 60]),
}
BODY_H = {"hero": PT.HERO_H / 7.3, "partner": PT.PARTNER_H / 7.3}   # 頭1つ分（px）


def person_points(kp, h, view, base_z):
    """関節を3次元にする。横向きの構図は右側（r）を手前、左側（l）を奥に置く"""
    out = {}
    for n, (x, y) in kp.items():
        z = base_z
        if view == "side":
            if n[0] == "r" and n != "rear" and n != "reye":
                z -= h * 0.7
            elif n[0] == "l" and n != "lear" and n != "leye":
                z += h * 0.7
        out[n] = np.array([x, y, z], float)
    return out


def capsules(p, h, scale):
    """成人の比率の人形：(始点, 終点, 半径) のリスト"""
    s = h * scale / h if h else 1.0
    C = []
    def cap(a, b, r):
        if a in p and b in p:
            C.append((p[a], p[b], r))
    def mid(a, b):
        return (p[a] + p[b]) / 2 if a in p and b in p else None
    # 頭（鼻と首の間から少し上）
    if "nose" in p and "neck" in p:
        head = p["nose"] * 0.6 + p["neck"] * 0.4
        head = head + (p["nose"] - p["neck"]) * 0.25
        C.append((head, head, h * 0.5))
        cap("neck", "nose", h * 0.2)
    ms, mh = mid("rsho", "lsho"), mid("rhip", "lhip")
    if ms is not None and mh is not None:
        C.append((ms, mh, h * 0.62))                       # 胴（胸の厚み）
        C.append((ms * 0.7 + mh * 0.3, ms * 0.7 + mh * 0.3, h * 0.72))   # 胸
        C.append((mh, mh, h * 0.62))                       # 腰
        C.append((p["neck"], ms, h * 0.3)) if "neck" in p else None
    for a, b in (("rsho", "lsho"), ("rhip", "lhip")):
        cap(a, b, h * 0.35)
    for s_ in "rl":
        cap(s_ + "sho", s_ + "elb", h * 0.22); cap(s_ + "elb", s_ + "wri", h * 0.18)
        cap(s_ + "hip", s_ + "knee", h * 0.33); cap(s_ + "knee", s_ + "ank", h * 0.24)
        if s_ + "wri" in p:
            C.append((p[s_ + "wri"], p[s_ + "wri"], h * 0.2))
        if s_ + "ank" in p:
            C.append((p[s_ + "ank"], p[s_ + "ank"], h * 0.2))
    return C


def render(caps):
    """正射影の z バッファ：丸い筒（球を並べたもの）の手前側の表面の奥行き"""
    zbuf = np.full((H, W), np.inf)
    yy, xx = np.mgrid[0:H, 0:W]
    for a, b, r in caps:
        L = np.linalg.norm(b[:2] - a[:2]) + abs(b[2] - a[2])
        n = max(1, int(L / max(2.0, r * 0.25)))
        for t in np.linspace(0, 1, n + 1):
            c = a + (b - a) * t
            x0, x1 = int(max(0, c[0] - r)), int(min(W, c[0] + r + 1))
            y0, y1 = int(max(0, c[1] - r)), int(min(H, c[1] + r + 1))
            if x0 >= x1 or y0 >= y1:
                continue
            dx = xx[y0:y1, x0:x1] - c[0]; dy = yy[y0:y1, x0:x1] - c[1]
            d2 = r * r - dx * dx - dy * dy
            m = d2 > 0
            z = c[2] - np.sqrt(np.where(m, d2, 0))
            sub = zbuf[y0:y1, x0:x1]
            np.minimum(sub, np.where(m, z, np.inf), out=sub)
    return zbuf


def to_image(zbuf):
    m = np.isfinite(zbuf)
    img = np.zeros((H, W), np.uint8)
    if m.any():
        zmin, zmax = zbuf[m].min(), zbuf[m].max()
        v = 1 - (zbuf[m] - zmin) / max(1e-6, zmax - zmin)     # 手前ほど 1
        img[m] = (60 + v * 195).astype(np.uint8)              # 人形は 60〜255、背景は 0
    return Image.fromarray(img).convert("RGB")


def build():
    P = PT.poses()
    for pid in PT.MIRROR:
        P[pid + "_r"] = [PT.mirror(k) for k in P[pid]]
        META[pid + "_r"] = META[pid]
        PT.ROLES[pid + "_r"] = PT.ROLES[pid]
    out = {}
    for pid, people in P.items():
        view, pz = META[pid]
        caps = []
        for kp, role, z in zip(people, PT.ROLES[pid], pz):
            # 横たわる構図は 0.7倍、床に座る足コキは 0.8倍で描いているので頭の大きさも合わせる
            scale = 0.7 if pid.startswith(("lying", "girl_on_top", "legs_up")) else 0.8 if pid == "standing_foot" else \
                    0.75 if pid.startswith("all_fours") else 0.95 if pid == "arms_up_bound" else 1.0
            h = BODY_H[role] * scale
            caps += capsules(person_points(kp, h, view, z), h, scale)
        out[pid] = to_image(render(caps))
    return out


def main():
    os.makedirs(PT.OUT, exist_ok=True)
    imgs = build()
    for pid, im in imgs.items():
        p = os.path.join(PT.OUT, "depth_%s.png" % pid)
        im.save(p); shutil.copy2(p, os.path.join(PT.COMFY_IN, "pose_depth_%s.png" % pid))
        print("奥行き下書き:", pid)
    if "--preview" in sys.argv:
        ks = sorted(imgs)
        sheet = Image.new("RGB", (210 * len(ks), 310), (40, 40, 40))
        for i, k in enumerate(ks):
            sheet.paste(imgs[k].resize((206, 302)), (i * 210 + 2, 4))
        sheet.save(os.path.join(PT.OUT, "_奥行き一覧.png"))


if __name__ == "__main__":
    main()
