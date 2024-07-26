## 如何设置系统
- 参照 https://www.raspberrypi.com/software/  进行镜像安装
    - https://github.com/conda-forge/miniforge 这个比miniconda更好
- 进行特殊版本的conda安装，https://pan.si.sjtu.edu.cn/f/d17bd97258de4209bffd/?dl=1
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 等设置
- conda create -n py310 python=310 环境
- conda activate py310
- git clone yolov5.git
- pip install -r requirements.txt
    - 需要注意的是我们需要安装特定版本的torch==1.10.2 torchvision==0.11.3
