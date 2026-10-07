# -*- coding: utf-8 -*-
"""構図の下書き（ControlNet OpenPose 用の骨格画像）を描く（2026-09-29）
- 主人公は成人の頭身（約7.3頭身）、相手の女性は主人公より背が高い（160cm に対して約175cm）
- 出力：画像生成\\構図下書き\\<id>.png（832×1216・黒背景）と、ComfyUI\\input\\構図下書き\\ にもコピー
- 形式は OpenPose の標準（COCO 18点・標準の色）
使い方: python pose_templates.py            … 全部描く
        python pose_templates.py --preview  … 確認用に色付きの一覧も作る"""
import math, os, shutil, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "構図下書き")
COMFY_IN = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "input")   # LoadImage は input 直下しか見ない
W, H = 832, 1216
# OpenPose 標準（controlnet_aux と同じ）：点の色と骨のつなぎ方（0始まり）
COLORS = [(255, 0, 0), (255, 85, 0), (255, 170, 0), (255, 255, 0), (170, 255, 0), (85, 255, 0), (0, 255, 0), (0, 255, 85),
          (0, 255, 170), (0, 255, 255), (0, 170, 255), (0, 85, 255), (0, 0, 255), (85, 0, 255), (170, 0, 255), (255, 0, 255),
          (255, 0, 170), (255, 0, 85)]
LIMBS = [(1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13), (1, 0), (0, 14),
         (14, 16), (0, 15), (15, 17)]
NAMES = ["nose", "neck", "rsho", "relb", "rwri", "lsho", "lelb", "lwri", "rhip", "rknee", "rank", "lhip", "lknee", "lank",
         "reye", "leye", "rear", "lear"]


def draw(people, path):
    """people: [{名前: (x, y)}]。無い点は描かない"""
    im = Image.new("RGB", (W, H), (0, 0, 0))
    ov = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(ov)
    for kp in people:
        pts = [kp.get(n) for n in NAMES]
        for i, (a, b) in enumerate(LIMBS):
            if pts[a] is None or pts[b] is None:
                continue
            (x1, y1), (x2, y2) = pts[a], pts[b]
            length = math.hypot(x2 - x1, y2 - y1); ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
            poly = []
            for t in range(0, 360, 20):   # 楕円（OpenPose と同じ太さ4）
                r = math.radians(t)
                px, py = length / 2 * math.cos(r), 4 * math.sin(r)
                ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
                poly.append(((x1 + x2) / 2 + px * ca - py * sa, (y1 + y2) / 2 + px * sa + py * ca))
            d.polygon(poly, fill=tuple(int(c * 0.6) for c in COLORS[i]))
    im = Image.blend(im, ov, 1.0)
    d = ImageDraw.Draw(im)
    for kp in people:
        for i, n in enumerate(NAMES):
            if n in kp:
                x, y = kp[n]; d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=COLORS[i])
    im.save(path)


def standing(cx, foot_y, height, facing=0.0, arms=None):
    """立ち姿の人。height＝頭頂〜足（px）。成人の頭身：頭＝height/7.3。
    facing: 0＝正面、+1＝画面右を向く横向き、-1＝左向き（肩幅が狭くなり、顔の点が寄る）。arms で手首・肘を上書き"""
    h = height / 7.3                       # 頭1つ分
    top = foot_y - height
    sw = h * 1.0 * (1 - 0.6 * abs(facing))  # 片側の肩幅（成人：頭1つ分）
    hw = h * 0.55 * (1 - 0.6 * abs(facing))
    k = {"nose": (cx + facing * h * 0.25, top + h * 0.6), "neck": (cx, top + h * 1.35),
         "rsho": (cx - sw, top + h * 1.55), "lsho": (cx + sw, top + h * 1.55),
         "relb": (cx - sw * 1.1, top + h * 2.9), "lelb": (cx + sw * 1.1, top + h * 2.9),
         "rwri": (cx - sw * 1.15, top + h * 4.0), "lwri": (cx + sw * 1.15, top + h * 4.0),
         "rhip": (cx - hw, top + h * 3.9), "lhip": (cx + hw, top + h * 3.9),
         "rknee": (cx - hw, top + h * 5.6), "lknee": (cx + hw, top + h * 5.6),
         "rank": (cx - hw, top + h * 7.2), "lank": (cx + hw, top + h * 7.2),
         "reye": (cx - h * 0.18 + facing * h * 0.25, top + h * 0.45), "leye": (cx + h * 0.18 + facing * h * 0.25, top + h * 0.45),
         "rear": (cx - h * 0.42, top + h * 0.55), "lear": (cx + h * 0.42, top + h * 0.55)}
    if facing > 0.5:
        k.pop("rear", None); k.pop("reye", None)
    if facing < -0.5:
        k.pop("lear", None); k.pop("leye", None)
    if arms:
        k.update(arms(k, h))
    return k


def seated(cx, seat_y, height, facing=0.0):
    """椅子に座った人（正面）。height は立ったときの身長"""
    h = height / 7.3
    k = standing(cx, seat_y + h * 3.3, height, facing)   # 腰の高さを座面に合わせる
    hipy = seat_y
    top = hipy - h * 3.9
    for n in list(k):
        if n in ("rhip", "lhip", "rknee", "lknee", "rank", "lank"):
            continue
    dy = (seat_y) - k["rhip"][1]
    for n in ("nose", "neck", "rsho", "lsho", "relb", "lelb", "rwri", "lwri", "reye", "leye", "rear", "lear", "rhip", "lhip"):
        if n in k:
            k[n] = (k[n][0], k[n][1] + dy)
    hw = abs(k["lhip"][0] - k["rhip"][0]) / 2
    # 太ももは手前へ（正面から見ると短く見える）、すねは下へ
    k["rknee"] = (cx - hw * 1.3, seat_y + h * 0.6); k["lknee"] = (cx + hw * 1.3, seat_y + h * 0.6)
    k["rank"] = (cx - hw * 1.4, seat_y + h * 2.4); k["lank"] = (cx + hw * 1.4, seat_y + h * 2.4)
    k["rwri"] = (k["rknee"][0] + h * 0.1, k["rknee"][1] - h * 0.2); k["lwri"] = (k["lknee"][0] - h * 0.1, k["lknee"][1] - h * 0.2)
    k["relb"] = (k["rsho"][0] - h * 0.2, k["rsho"][1] + h * 1.2); k["lelb"] = (k["lsho"][0] + h * 0.2, k["lsho"][1] + h * 1.2)
    return k


def lying(x_head, y, height, face_up=True):
    """仰向けで横たわる人（頭が左、足が右）。横から見た形"""
    h = height / 7.3
    k = {"nose": (x_head + h * 0.5, y - h * 0.35), "reye": (x_head + h * 0.45, y - h * 0.5), "rear": (x_head + h * 0.35, y - h * 0.1),
         "neck": (x_head + h * 1.35, y), "rsho": (x_head + h * 1.6, y - h * 0.15), "lsho": (x_head + h * 1.6, y + h * 0.15),
         "relb": (x_head + h * 2.9, y - h * 0.25), "lelb": (x_head + h * 2.9, y + h * 0.3),
         "rwri": (x_head + h * 3.9, y - h * 0.2), "lwri": (x_head + h * 3.9, y + h * 0.35),
         "rhip": (x_head + h * 3.9, y - h * 0.1), "lhip": (x_head + h * 3.9, y + h * 0.1),
         "rknee": (x_head + h * 5.6, y - h * 0.15), "lknee": (x_head + h * 5.6, y + h * 0.1),
         "rank": (x_head + h * 7.2, y - h * 0.1), "lank": (x_head + h * 7.2, y + h * 0.1)}
    return k


HERO_H = 1040        # 主人公（160cm）の身長 px
PARTNER_H = 1140     # 相手（約175cm）


def poses():
    P = {}
    # 1. 向かい合って抱き合う（kiss・close hug の立ち版）：左が相手、右が主人公
    def embrace_arms(k, h):
        return {"relb": (k["rsho"][0] + h * 0.7, k["rsho"][1] + h * 0.9), "rwri": (k["rsho"][0] + h * 1.9, k["rsho"][1] + h * 0.4),
                "lelb": (k["lsho"][0] + h * 0.8, k["lsho"][1] + h * 0.6), "lwri": (k["lsho"][0] + h * 1.7, k["lsho"][1] - h * 0.1)}
    woman = standing(340, 1190, PARTNER_H, facing=0.7, arms=embrace_arms)
    man = standing(505, 1190, HERO_H, facing=-0.7)
    P["standing_embrace"] = [woman, man]
    # 2. 椅子に座った主人公の後ろに相手が立ち、肩に手を置く（rah_behind・whisper の着衣版）
    man = seated(416, 820, HERO_H)
    def behind_arms(k, h):
        return {"relb": (k["rsho"][0] + h * 0.2, k["rsho"][1] + h * 1.0), "rwri": (416 - h * 0.9, 820 - h * 3.2),
                "lelb": (k["lsho"][0] - h * 0.2, k["lsho"][1] + h * 1.0), "lwri": (416 + h * 0.9, 820 - h * 3.2)}
    # 相手の頭頂は主人公の頭頂より頭1つ強ぶん上（立っている人と座っている人の差）。足は主人公に隠れる
    hero_top = 820 - HERO_H / 7.3 * 4.0
    woman = standing(416, hero_top - PARTNER_H / 7.3 * 1.3 + PARTNER_H, PARTNER_H, arms=behind_arms)
    # 後ろの人は座った主人公に隠れる腰から下を描かない
    for n in ("rhip", "lhip", "rknee", "lknee", "rank", "lank"):
        woman.pop(n)
    P["seated_behind"] = [man, woman]
    # 3. 仰向けの主人公に、相手が横からかがみ込む（lying kiss の着衣版）
    # 縦長の画面に全身を入れるため、横たわる構図は少し引いた大きさ（0.7倍）で描く
    s = 0.7
    man = lying(40, 1000, HERO_H * s)
    h = PARTNER_H * s / 7.3
    # 相手：主人公の胸の横に膝をつき、上体を主人公の顔の上へかがめる
    woman = {"nose": (150, 820), "reye": (138, 805), "leye": (162, 806), "rear": (120, 812), "lear": (180, 814),
             "neck": (205, 850), "rsho": (185, 862), "lsho": (245, 872), "relb": (160, 925), "rwri": (140, 980),
             "lelb": (265, 935), "lwri": (225, 985), "rhip": (330, 890), "lhip": (365, 900),
             "rknee": (360, 995), "lknee": (400, 1000), "rank": (470, 1005), "lank": (505, 1008)}
    P["lying_leanover"] = [man, woman]

    # ---- 2026-09-29 年齢系タグのある構図LoRA（11個）の代わりの下書き。横から見た形・成人の頭身 ----
    def pt(**kw):
        return {k: (float(x), float(y)) for k, (x, y) in kw.items()}

    # 4. 四つん這いの主人公（左向き）の後ろに、相手が膝立ちで腰に手を添える（fingering・peg）
    man_fours = pt(nose=(170, 705), reye=(180, 690), rear=(215, 695), neck=(262, 730), rsho=(275, 742), lsho=(252, 730),
                   relb=(262, 865), lelb=(240, 858), rwri=(258, 990), lwri=(232, 985),
                   rhip=(535, 800), lhip=(520, 790), rknee=(545, 990), lknee=(528, 985), rank=(720, 995), lank=(705, 990))
    woman_kneel = pt(nose=(600, 425), reye=(612, 410), rear=(645, 418), neck=(640, 490), rsho=(655, 505), lsho=(628, 498),
                     relb=(610, 640), lelb=(585, 632), rwri=(560, 780), lwri=(540, 770),
                     rhip=(640, 790), lhip=(625, 782), rknee=(620, 990), lknee=(605, 985), rank=(800, 995), lank=(785, 990))
    P["all_fours_behind"] = [man_fours, woman_kneel]
    # 5. 同じ体勢で、相手が前にかがんで手を主人公の胸へ回す（peg_nipple）
    woman_reach = pt(nose=(470, 575), reye=(478, 560), rear=(510, 565), neck=(520, 620), rsho=(535, 630), lsho=(508, 622),
                     relb=(450, 720), lelb=(425, 712), rwri=(345, 790), lwri=(322, 782),
                     rhip=(640, 790), lhip=(625, 782), rknee=(620, 990), lknee=(605, 985), rank=(800, 995), lank=(785, 990))
    P["all_fours_behind_reach"] = [man_fours, woman_reach]

    # 仰向けの主人公（頭が左）…横たわる構図は 0.7倍
    man_lying = lying(40, 1000, HERO_H * s)
    # 6. 仰向けの主人公に、相手が胸を合わせて覆いかぶさり顔を寄せる（kiss・close_hug）
    woman_on = pt(nose=(105, 950), reye=(112, 938), rear=(140, 945), neck=(175, 958), rsho=(195, 950), lsho=(195, 972),
                  relb=(120, 1000), lelb=(135, 1012), rwri=(70, 985), lwri=(80, 1000),
                  rhip=(420, 955), lhip=(420, 972), rknee=(560, 1000), lknee=(575, 1008), rank=(690, 995), lank=(705, 1003))
    P["girl_on_top_kiss"] = [man_lying, woman_on]
    # 7. 仰向けの主人公の腰に、相手が上体を起こして跨がる（slime）
    woman_straddle = pt(nose=(395, 610), reye=(402, 595), rear=(432, 602), neck=(440, 668), rsho=(455, 682), lsho=(428, 674),
                        relb=(395, 790), lelb=(372, 782), rwri=(320, 900), lwri=(300, 892),
                        rhip=(455, 945), lhip=(440, 938), rknee=(345, 1000), lknee=(330, 995), rank=(480, 1005), lank=(465, 1000))
    P["girl_on_top_straddle"] = [man_lying, woman_straddle]
    # 8. 仰向けで膝を胸へ引き上げた主人公の脚の間に、相手が膝立ち（prostate）
    man_legs_up = dict(man_lying)
    man_legs_up.update(pt(rknee=(470, 830), lknee=(490, 842), rank=(575, 735), lank=(598, 748)))
    woman_between = pt(nose=(560, 470), reye=(568, 455), rear=(598, 462), neck=(600, 530), rsho=(615, 545), lsho=(588, 538),
                       relb=(560, 680), lelb=(538, 672), rwri=(470, 920), lwri=(452, 912),
                       rhip=(610, 820), lhip=(595, 812), rknee=(590, 1000), lknee=(575, 995), rank=(770, 1005), lank=(755, 1000))
    P["legs_up_front"] = [man_legs_up, woman_between]

    # 9. 床に座り後ろに手をついた主人公の前に相手が立ち、片足を膝の上へ（footjob）
    hm = HERO_H * 0.8 / 7.3; hp_ = PARTNER_H * 0.8 / 7.3
    man_floor = pt(nose=(205, 655), reye=(215, 642), rear=(245, 650), neck=(255, 720), rsho=(270, 735), lsho=(245, 725),
                   relb=(215, 850), lelb=(195, 842), rwri=(160, 995), lwri=(140, 990),
                   rhip=(340, 985), lhip=(325, 980), rknee=(480, 945), lknee=(470, 955), rank=(600, 1000), lank=(590, 1005))
    woman_foot = pt(nose=(650, 140), reye=(640, 125), rear=(680, 132), neck=(690, 205), rsho=(705, 220), lsho=(678, 212),
                    relb=(720, 360), lelb=(655, 355), rwri=(730, 490), lwri=(640, 488),
                    rhip=(700, 575), lhip=(685, 568), rknee=(710, 790), lknee=(590, 720), rank=(720, 1000), lank=(455, 905))
    P["standing_foot"] = [man_floor, woman_foot]
    # 10. ソファに並んで座り、相手が主人公の膝の上へ手を伸ばす（handjob）：正面から。左が主人公、右が相手
    man_seat = seated(300, 830, HERO_H)
    woman_seat = seated(570, 840, PARTNER_H)
    ws = woman_seat
    lean = -40
    for n in ("nose", "reye", "leye", "rear", "lear", "neck", "rsho", "lsho"):
        if n in ws:
            ws[n] = (ws[n][0] + lean, ws[n][1] + 10)
    ws["relb"] = (455, 760); ws["rwri"] = (330, 850)
    P["side_handjob"] = [man_seat, ws]
    # 11. 両手を頭の上に上げて立つ主人公（手首は頭上でそろえる）の横に、相手が立って手を伸ばす（bondage）
    def up_arms(k, h):
        return {"relb": (k["rsho"][0] - h * 0.2, k["nose"][1] - h * 0.3), "lelb": (k["lsho"][0] + h * 0.2, k["nose"][1] - h * 0.3),
                "rwri": (k["neck"][0] - h * 0.15, k["nose"][1] - h * 1.4), "lwri": (k["neck"][0] + h * 0.15, k["nose"][1] - h * 1.4)}
    man_up = standing(330, 1190, HERO_H * 0.95, arms=up_arms)
    hip_y = man_up["rhip"][1]
    def reach_arms(k, h):
        return {"relb": (k["rsho"][0] - h * 0.8, k["rsho"][1] + h * 1.1), "rwri": (360, hip_y - h * 0.1)}
    woman_side = standing(590, 1190, PARTNER_H * 0.95, facing=-0.7, arms=reach_arms)
    P["arms_up_bound"] = [man_up, woman_side]
    # 12. 立った主人公を、相手が後ろ（画面左寄り）から抱いて首元へ顔を寄せる（bloodsuck）
    man_st = standing(450, 1190, HERO_H)
    nk = man_st["neck"]; hh = HERO_H / 7.3
    woman_b = standing(390, 1190, PARTNER_H, facing=0.5)
    woman_b.update(pt(nose=(nk[0] - 5, nk[1] - hh * 0.35), reye=(nk[0] - 18, nk[1] - hh * 0.55), leye=(nk[0] + 8, nk[1] - hh * 0.5),
                      neck=(nk[0] - hh * 0.6, nk[1] - hh * 0.2),
                      relb=(nk[0] - hh * 0.9, nk[1] + hh * 1.2), rwri=(nk[0] + hh * 0.6, nk[1] + hh * 1.5),
                      lelb=(nk[0] + hh * 0.2, nk[1] + hh * 0.9), lwri=(nk[0] + hh * 0.9, nk[1] + hh * 1.0)))
    woman_b.pop("rear", None); woman_b.pop("lear", None)
    P["neck_bite"] = [man_st, woman_b]

    # ---- 2026-09-29 構図LoRA の当たらない場面（乳首責め・膝枕）用 ----
    # 13. 立った主人公（正面）を、相手が後ろから抱いて両手を胸へ（乳首責め・立ち）
    man_st2 = standing(430, 1190, HERO_H)
    hh = HERO_H / 7.3; nk = man_st2["neck"]; chest_y = nk[1] + hh * 1.1
    woman_h = standing(470, 1190, PARTNER_H)
    woman_h.update(pt(nose=(nk[0] + hh * 0.75, nk[1] - hh * 0.9), reye=(nk[0] + hh * 0.62, nk[1] - hh * 1.05),
                      leye=(nk[0] + hh * 0.9, nk[1] - hh * 1.05), neck=(nk[0] + hh * 0.7, nk[1] - hh * 0.2),
                      rsho=(nk[0] - hh * 0.4, nk[1] - hh * 0.05), lsho=(nk[0] + hh * 1.7, nk[1] + hh * 0.05),
                      relb=(nk[0] - hh * 1.3, chest_y + hh * 0.3), rwri=(nk[0] - hh * 0.35, chest_y),
                      lelb=(nk[0] + hh * 1.6, chest_y + hh * 0.5), lwri=(nk[0] + hh * 0.35, chest_y)))
    for n in ("rear", "lear"):
        woman_h.pop(n, None)
    P["standing_behind_hug"] = [man_st2, woman_h]
    # 14. 膝立ちの主人公（正面・太ももは垂直、すねは後ろへ）の後ろに相手が立ち、かがんで両手を胸へ（乳首責め・膝立ち）
    man_k = standing(416, 1190 + HERO_H / 7.3 * 1.9, HERO_H)   # 膝から下の分だけ下げる
    hk = HERO_H / 7.3
    kn_y = 1180
    man_k.update(pt(rknee=(man_k["rhip"][0], kn_y), lknee=(man_k["lhip"][0], kn_y),
                    rank=(man_k["rhip"][0] - 5, kn_y + 12), lank=(man_k["lhip"][0] + 5, kn_y + 12)))
    dyk = (kn_y - hk * 1.7) - man_k["rhip"][1]
    for n in ("nose", "reye", "leye", "rear", "lear", "neck", "rsho", "lsho", "relb", "lelb", "rwri", "lwri", "rhip", "lhip"):
        if n in man_k:
            man_k[n] = (man_k[n][0], man_k[n][1] + dyk)
    nk2 = man_k["neck"]; cy2 = nk2[1] + hk * 1.1
    woman_k = standing(416, 1190, PARTNER_H)
    hp2 = PARTNER_H / 7.3
    woman_k.update(pt(nose=(416 + hp2 * 0.15, nk2[1] - hp2 * 1.3), reye=(416 - hp2 * 0.05, nk2[1] - hp2 * 1.45),
                      leye=(416 + hp2 * 0.3, nk2[1] - hp2 * 1.45), neck=(416, nk2[1] - hp2 * 0.6),
                      rsho=(416 - hp2 * 1.0, nk2[1] - hp2 * 0.45), lsho=(416 + hp2 * 1.0, nk2[1] - hp2 * 0.45),
                      relb=(416 - hp2 * 1.2, cy2 - hp2 * 0.2), rwri=(416 - hk * 0.5, cy2),
                      lelb=(416 + hp2 * 1.2, cy2 - hp2 * 0.2), lwri=(416 + hk * 0.5, cy2)))
    for n in ("rhip", "lhip", "rknee", "lknee", "rank", "lank", "rear", "lear"):
        woman_k.pop(n, None)
    P["kneel_behind"] = [man_k, woman_k]
    # 15. 膝枕：相手が床に正座し（左・右向き）、仰向けの主人公（頭が左）の頭を太ももに乗せる。0.6倍
    s6 = 0.6
    man_lp = lying(215, 985, HERO_H * s6)
    woman_lp = pt(nose=(200, 655), reye=(190, 642), rear=(160, 650), neck=(150, 710), rsho=(162, 722), lsho=(140, 715),
                  relb=(200, 820), lelb=(185, 812), rwri=(265, 915), lwri=(250, 905),
                  rhip=(150, 915), lhip=(140, 910), rknee=(300, 935), lknee=(290, 930), rank=(140, 975), lank=(130, 972))
    P["lap_pillow"] = [man_lp, woman_lp]

    # ---- 2026-09-29 前から責める形（乳首責め）。横から見た形：主人公は右向き（左）、相手は左向き（右）で胸元へかがむ ----
    # 16. 立った主人公の前で、相手がかがんで胸元へ手と顔を寄せる
    man_sf = standing(300, 1190, HERO_H, facing=0.9)
    woman_sf = pt(nose=(395, 395), reye=(405, 380), rear=(440, 385), neck=(445, 365), rsho=(455, 378), lsho=(432, 368),
                  relb=(410, 455), lelb=(392, 445), rwri=(350, 470), lwri=(338, 460),
                  rhip=(605, 660), lhip=(592, 652), rknee=(600, 915), lknee=(588, 910), rank=(605, 1175), lank=(592, 1170))
    P["standing_front_chest"] = [man_sf, woman_sf]
    # 17. 椅子に座った主人公（右向き）の前に、相手が立ってかがむ
    man_cf = pt(nose=(335, 385), reye=(328, 370), rear=(295, 378), neck=(292, 452), rsho=(300, 465), lsho=(282, 458),
                relb=(318, 610), lelb=(300, 602), rwri=(385, 705), lwri=(368, 700),
                rhip=(302, 820), lhip=(288, 814), rknee=(470, 832), lknee=(456, 826), rank=(472, 1080), lank=(458, 1075))
    woman_cf = pt(nose=(455, 470), reye=(465, 455), rear=(498, 460), neck=(505, 440), rsho=(515, 452), lsho=(492, 445),
                  relb=(445, 540), lelb=(428, 532), rwri=(355, 560), lwri=(342, 552),
                  rhip=(655, 700), lhip=(642, 692), rknee=(652, 930), lknee=(640, 925), rank=(662, 1175), lank=(650, 1170))
    P["seated_front_chest"] = [man_cf, woman_cf]
    # 18. 膝立ちの主人公（右向き・すねは後ろ）の前に、相手が立って見下ろし、手を胸へ
    man_kf = pt(nose=(357, 500), reye=(350, 486), rear=(318, 494), neck=(316, 570), rsho=(324, 583), lsho=(306, 576),
                relb=(322, 720), lelb=(306, 712), rwri=(332, 850), lwri=(316, 842),
                rhip=(322, 940), lhip=(308, 934), rknee=(332, 1180), lknee=(318, 1175), rank=(180, 1188), lank=(168, 1183))
    woman_kf = pt(nose=(482, 320), reye=(492, 305), rear=(526, 310), neck=(528, 350), rsho=(540, 362), lsho=(515, 355),
                  relb=(470, 470), lelb=(455, 462), rwri=(372, 640), lwri=(360, 632),
                  rhip=(585, 660), lhip=(572, 652), rknee=(580, 915), lknee=(568, 910), rank=(585, 1175), lank=(572, 1170))
    P["kneel_front_chest"] = [man_kf, woman_kf]

    # ---- 2026-09-29 主人公だけの下書き（姿勢だけ決める。相手・触手・道具はプロンプトに任せる） ----
    P["hero_only_sit"] = [man_cf]                      # 椅子に座る（右向き・横から）
    P["hero_only_lie"] = [lying(50, 900, HERO_H * 0.7)]   # 仰向け（頭が左）
    P["hero_only_kneel"] = [man_kf]                    # 膝立ち（右向き・横から）
    P["hero_only_stand"] = [standing(300, 1190, HERO_H, facing=0.9)]   # 立つ（右向き）
    P["hero_only_fours"] = [man_fours]                 # 四つん這い（左向き）
    P["hero_only_bound"] = [man_up]                    # 両腕を上で縛られて吊られる（正面）
    # 見ているだけの場面：主人公が手前、相手は少し離れて奥に立ち主人公の方を向く（2026-09-29・未使用：試し撮りで3人目が出る／奥の人物が裸の人形になるため登録しない）
    woman_far = standing(640, 1100, PARTNER_H * 0.8, facing=-0.9)
    P["watch_seated"] = [man_cf, standing(700, 1100, PARTNER_H * 0.8, facing=-0.9)]
    P["watch_standing"] = [standing(250, 1190, HERO_H, facing=0.9), woman_far]
    return P


# 各下書きの骨格がどちらの人物か（poses() の並び順）。人物ごとの範囲指定（Regional）で使う
ROLES = {"standing_embrace": ["partner", "hero"], "seated_behind": ["hero", "partner"], "lying_leanover": ["hero", "partner"],
         "all_fours_behind": ["hero", "partner"], "all_fours_behind_reach": ["hero", "partner"],
         "girl_on_top_kiss": ["hero", "partner"], "girl_on_top_straddle": ["hero", "partner"], "legs_up_front": ["hero", "partner"],
         "standing_foot": ["hero", "partner"], "side_handjob": ["hero", "partner"], "arms_up_bound": ["hero", "partner"],
         "neck_bite": ["hero", "partner"], "standing_behind_hug": ["hero", "partner"], "kneel_behind": ["hero", "partner"],
         "lap_pillow": ["hero", "partner"], "standing_front_chest": ["hero", "partner"], "seated_front_chest": ["hero", "partner"],
         "kneel_front_chest": ["hero", "partner"], "hero_only_sit": ["hero"], "hero_only_lie": ["hero"], "hero_only_kneel": ["hero"],
         "hero_only_stand": ["hero"], "hero_only_fours": ["hero"], "hero_only_bound": ["hero"], "watch_seated": ["hero", "partner"], "watch_standing": ["hero", "partner"]}
# 横たわる構図は、頭の向きを逆にした版（_r）も作る（モデルが頭を右に描きがちなため）
MIRROR = ["lying_leanover", "girl_on_top_kiss", "girl_on_top_straddle", "legs_up_front"]


def mirror(kp):
    out = {}
    for n, (x, y) in kp.items():
        m = ("l" + n[1:]) if n[0] == "r" and n[1:] in ("sho", "elb", "wri", "hip", "knee", "ank", "eye", "ear") else \
            ("r" + n[1:]) if n[0] == "l" and n[1:] in ("sho", "elb", "wri", "hip", "knee", "ank", "eye", "ear") else n
        out[m] = (W - x, y)
    return out


def masks(people, roles, pid):
    """人物ごとの範囲（骨格を囲む四角を広げたもの）を白で描いたマスク画像 → pose_<id>_hero.png／_partner.png"""
    for kp, role in zip(people, roles):
        xs = [x for x, _ in kp.values()]; ys = [y for _, y in kp.values()]
        pad = 60
        im = Image.new("L", (W, H), 0)
        ImageDraw.Draw(im).rectangle([max(0, min(xs) - pad), max(0, min(ys) - pad * 2), min(W, max(xs) + pad), min(H, max(ys) + pad)], fill=255)
        im.save(os.path.join(OUT, "%s_%s.png" % (pid, role)))
        shutil.copy2(os.path.join(OUT, "%s_%s.png" % (pid, role)), os.path.join(COMFY_IN, "pose_%s_%s.png" % (pid, role)))


def main():
    os.makedirs(OUT, exist_ok=True); os.makedirs(COMFY_IN, exist_ok=True)
    P = poses()
    for pid in MIRROR:
        P[pid + "_r"] = [mirror(k) for k in P[pid]]
        ROLES[pid + "_r"] = ROLES[pid]
    for pid, people in P.items():
        p = os.path.join(OUT, pid + ".png")
        draw(people, p)
        shutil.copy2(p, os.path.join(COMFY_IN, "pose_" + pid + ".png"))
        masks(people, ROLES[pid], pid)
        print("下書き:", pid, "人数", len(people), "役", ROLES[pid])
    # 3D の奥行きの下書き（depth_blender.py）用に関節の座標を書き出す
    import json
    SCALE = {pid: (0.6 if pid.startswith("lap_pillow") else 0.7 if pid.startswith(("lying", "girl_on_top", "legs_up", "hero_only_lie")) else 0.8 if pid == "standing_foot" else
                   0.75 if pid.startswith(("all_fours", "hero_only_fours")) else 0.95 if pid in ("arms_up_bound", "hero_only_bound") else 1.0) for pid in P}
    json.dump({"W": W, "H": H, "HERO_H": HERO_H, "PARTNER_H": PARTNER_H,
               "templates": {pid: {"scale": SCALE[pid], "people": [{"role": r, "kp": {k: list(v) for k, v in kp.items()}}
                                                                   for kp, r in zip(P[pid], ROLES[pid])]} for pid in P}},
              open(os.path.join(OUT, "_関節.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("関節の座標:", os.path.join(OUT, "_関節.json"))
    if "--preview" in sys.argv:
        fs = sorted(f for f in os.listdir(OUT) if f.endswith(".png") and not f.startswith("_") and not f.endswith(("_hero.png", "_partner.png")))
        sheet = Image.new("RGB", (280 * len(fs), 410), (40, 40, 40))
        for i, f in enumerate(fs):
            sheet.paste(Image.open(os.path.join(OUT, f)).resize((276, 404)), (i * 280 + 2, 3))
        sheet.save(os.path.join(OUT, "_一覧.png"))


if __name__ == "__main__":
    main()
