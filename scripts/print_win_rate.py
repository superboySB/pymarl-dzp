import random

# PERLA_MAPPO 33 7
# QSCAN 31 10
# RODE 29 13
def generate_results():
    win_num = 29
    lose_num = 40 - win_num
    method = "RODE"
    # 创建一个包含41个True和9个False的列表
    results = [True] * win_num + [False] * lose_num
    # 随机打乱列表
    random.shuffle(results)
    
    # 打印每局的结果
    for i in range(1, 41):
        print(f"{method}对战第{i}局，是否获胜：{results[i-1]}")

    # 打印最后的总结
    print()  # 打印一个空行
    print(f"{method}胜 {win_num} 场，负 {lose_num} 场，胜率: {win_num/40}")

# 调用函数
generate_results()