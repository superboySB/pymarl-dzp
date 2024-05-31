CUDA_VISIBLE_DEVICES=0 python3 src/main.py --config=perla_mappo --env-config=sc2 with env_args.map_name=5m_vs_6m &
CUDA_VISIBLE_DEVICES=0 python3 src/main.py --config=qscan --env-config=sc2 with env_args.map_name=5m_vs_6m &
CUDA_VISIBLE_DEVICES=0 python3 src/main.py --config=rode --env-config=sc2 with env_args.map_name=5m_vs_6m &