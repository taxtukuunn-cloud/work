# -*- coding: utf-8 -*-
"""敵キャラLoRAを学習する（2026-09-29）。sd-scripts の venv の Python で実行する（C3_キャラ学習.bat から）。
Lora用\\chara\\toml\\<MOD>_*_<絵柄>.toml を順に学習 → Lora用\\output_chara\\ → ComfyUI\\models\\loras\\キャラ\\ にコピー。
設定は主人公LoRA（H3_学習_SDXL.bat）と同じ。loras\\キャラ に 8エポック目が既にあるキャラは飛ばす（--redo で学習し直す）。
使い方: python train_chara.py <MODコード> [--redo]"""
import glob, os, shutil, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CKPT = r"C:\Users\taku2\Downloads\ComfyUI_windows_portable\ComfyUI\models\checkpoints\waiIllustriousSDXL_v170.safetensors"
LORAS = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "models", "loras", "キャラ")
OUTD = os.path.join(ROOT, "output_chara")
args = [x for x in sys.argv[1:] if not x.startswith("--")]
redo = "--redo" in sys.argv
if not args:
    print("使い方: train_chara.py <MODコード> [--redo]"); sys.exit(1)
mod = args[0]
tomls = sorted(glob.glob(os.path.join(HERE, "toml", mod + "_*.toml")))
if not tomls:
    print("学習設定がありません（先に C2_キャラ学習データ作成.bat）。"); sys.exit(1)
os.makedirs(LORAS, exist_ok=True)
todo = []
for t in tomls:
    tag = os.path.basename(t)[:-5]            # <MOD>_<キャラ>_<絵柄>
    name = "chr_" + tag
    if not redo and os.path.isfile(os.path.join(LORAS, name + "-000008.safetensors")):
        print("  %s: 学習済み（飛ばす。やり直すなら --redo）" % name); continue
    todo.append((t, name))
print("学習するキャラ: %d（1キャラ 10〜15分ほど）" % len(todo))
for i, (t, name) in enumerate(todo, 1):
    t0 = time.time()
    print("\n===== [%d/%d] %s =====" % (i, len(todo), name), flush=True)
    cmd = [sys.executable, "sdxl_train_network.py",
           "--pretrained_model_name_or_path=" + CKPT, "--dataset_config=" + t,
           "--output_dir=" + OUTD, "--output_name=" + name, "--save_model_as=safetensors",
           "--network_module=networks.lora", "--network_dim=16", "--network_alpha=8", "--network_train_unet_only",
           "--learning_rate=1e-4", "--optimizer_type=AdamW8bit", "--lr_scheduler=cosine", "--lr_warmup_steps=30",
           "--max_train_epochs=10", "--save_every_n_epochs=2",
           "--mixed_precision=bf16", "--save_precision=fp16", "--gradient_checkpointing", "--sdpa", "--no_half_vae",
           "--cache_latents", "--cache_latents_to_disk", "--max_data_loader_n_workers=0", "--seed=42"]
    r = subprocess.run(cmd, cwd=os.path.join(ROOT, "sd-scripts"))
    if r.returncode != 0:
        print("[エラー] %s の学習が止まりました。上のエラーを確認してください。" % name); sys.exit(1)
    for f in glob.glob(os.path.join(OUTD, name + "*.safetensors")):
        shutil.copy2(f, os.path.join(LORAS, os.path.basename(f)))
    print("  → loras\\キャラ\\ にコピー（%d分）" % ((time.time() - t0) // 60))
print("\n全部終わりました。ComfyUI を再起動すると、イベント画像で自動で使われます。")
