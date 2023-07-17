import os

os.system("python -X utf8 tools/diffusion/inference.py --config configs/svc_cn_hubert_soft_ms.py --checkpoint models/ys35/ys35.ckpt --speaker_mapping models/ys35/spk_map.json --gradio")

#python -X utf8 tools/diffusion/inference.py --config configs/svc_cn_hubert_soft_ms.py --checkpoint models/ys35/ys35.ckpt --speaker_mapping models/ys35/spk_map.json --gradioS