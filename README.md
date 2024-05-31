# 实验流程

配置星际争霸环境
```sh
bash scripts/install_dependencies.sh
source activate smac_py38
```

一键运行训练脚本`run.sh`，相当运行PERLA_MAPPO以及两个baseline QSCAN和RODE在5m_vs_6m的效果：
```sh
CUDA_VISIBLE_DEVICES=0 python3 src/main.py --config=perla_mappo --env-config=sc2 with env_args.map_name=5m_vs_6m
CUDA_VISIBLE_DEVICES=0 python3 src/main.py --config=qscan --env-config=sc2 with env_args.map_name=5m_vs_6m
CUDA_VISIBLE_DEVICES=0 python3 src/main.py --config=rode --env-config=sc2 with env_args.map_name=5m_vs_6m
```
中途停止训练`stop.sh`。

可以看到训练正常进行之后会有相应的ckpt文件，然后分别设置一下`checkpoint_path=$MODEL_DIR`、`runner='episide'`、`evaluate=True`以及`save_replay=True`。之后生成相应的replay文件在`/home/ps/pymarl/3rdparty/StarCraftII/Replays`目录，然后换成windows页面运行：
```sh
python -m pysc2.bin.play --norender --rgb_minimap_size 0 --replay NAME.SC2Replay
```