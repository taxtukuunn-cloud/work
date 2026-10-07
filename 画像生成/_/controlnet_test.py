# -*- coding: utf-8 -*-
"""構図の下書き（ControlNet）の試し撮り：着衣の2人で、下書きあり／なしを同じシードで比べる（2026-09-29）
→ ComfyUI\\output\\下書き確認\\<下書き>_<あり|なし>_"""
import json, os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.argv = [sys.argv[0]] + sys.argv[1:]
import gen

MODEL_NAME = sys.argv[1] if len(sys.argv) > 1 else ""
BASE = ("masterpiece, best quality, amazing quality, general, 1girl, 1boy, fully clothed, "
        "a tall adult woman with long silver hair and red eyes wearing a black long coat and a white blouse, "
        "the navy-haired man: adult man with navy blue hair, aqua eyes, white shirt, brown vest, dark trousers, "
        "he is shorter than the woman, ")
TESTS = {
    "standing_embrace": BASE + "standing face to face, the woman hugs him around the neck, close embrace, full body, indoors, room, detailed background",
    "seated_behind": BASE + "he sits on a wooden chair facing the viewer, the woman stands behind the chair with her hands on his shoulders, indoors, room, detailed background",
    "lying_leanover": BASE + "he lies on his back on a bed, the woman kneels beside the bed and leans over his face, from side, indoors, bedroom, detailed background",
}
NEG = "lowres, worst quality, bad anatomy, bad hands, extra limbs, nsfw, nude, text, watermark"


def main():
    gen.MODEL = gen.load_model("wai")
    gen.load_face_detail(); gen.load_pose_control()
    if MODEL_NAME:
        gen.POSE_CONTROL["model"] = MODEL_NAME
        gen.POSE_CONTROL["union_type"] = "openpose" if "union" in MODEL_NAME else ""

    class A: no_lora = False; no_hero = False; lora_strength = None; hero_strength = None
    lora = gen.load_lora(A()); lora["style"]["enabled"] = lora["hero"]["enabled"] = False
    tag = "union" if "union" in MODEL_NAME else "noob"
    for pid, pos in TESTS.items():
        for with_ctrl in (True, False):
            gen.FORCE_CONTROL = pid if with_ctrl else None
            gen.NO_CONTROL = not with_ctrl
            w, used = gen.wf({"positive": pos, "negative": NEG}, 777, 1,
                             "下書き確認/%s_%s_%s" % (pid, tag, "あり" if with_ctrl else "なし"), json.loads(json.dumps(lora)), False, name="下書き確認")
            urllib.request.urlopen(urllib.request.Request(gen.SERVER + "/prompt", data=json.dumps({"prompt": w}).encode("utf-8"),
                                                          headers={"Content-Type": "application/json"}), timeout=30)
            print("送信", pid, "下書き" + ("あり" if with_ctrl else "なし"), used)


if __name__ == "__main__":
    main()
