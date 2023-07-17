# 安装方法
把Releases 里面的env，model下载下来，解压到项目根目录里面

安装miniconda，打开

[换源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

安装[pytorch](https://pytorch.org/get-started/locally/) 

cpu==>pip3 install torch torchvision torchaudio 

cuda118==>pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

如果你选择的cpuenv，可以不用安装pytorch

创建一个目录链接（快捷方式），也可以把.cache文件夹直接移动到"C:\Users\你的用户名\" 

（选择跳过）运行管理员身份的cmd

运行 mklink /j C:\Users\\"你的用户名"\\.cache "你解压的.cache文件夹目录（你可以选择一个）" 

example     mklink /j C:\Users\user\.cache  "D:\cache"

运行pip install -e.

运行python startweb.py 或

python -X utf8 tools/diffusion/inference.py --config configs/svc_cn_hubert_soft_ms.py --checkpoint models/ys35/ys35.ckpt --speaker_mapping models/ys35/spk_map.json --gradioS
