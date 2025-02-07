# 用于发布ViTai Simulator
## 环境要求

Python==3.12.*

```
支持ubuntu 24.04
```


------

### Python环境准备


1. 创建`python3.12`虚拟环境

   ```bash
   conda create -n py312 python=3.12
   ```

2. 激活`python3.12`虚拟环境

   ```bash
   conda activate py312
   ```

3. 使用虚拟环境的pip安装pyvitaisimulator whl包，同时会联网下载其他所需的依赖库（需保证主机网络通畅）

4. 安装完成后，即可使用main.py中代码进行测试

   ```
   python main.py
   ```
   
5. 提供包括hand-e手爪和Realman手爪夹持cube、夹持cuboid、夹持cylinder、插孔仿真演示

6. simulator操控方式
   ```
   控制手爪的位置：左右箭头、B和F键、上下箭头
   控制手爪的姿态：Q/W、A/S、Z/X
   鼠标左键：控制旋转视角
   鼠标右键：控制平移视角
   鼠标滚轮：控制缩放视角
   运动速度加减：+-键
   退出程序：Q键
   ```
   

## 反馈

   如果你发现了任何错误，请联系我们！！！

   欢迎在该Github仓库提issues.