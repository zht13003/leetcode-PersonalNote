"""
https://leetcode-cn.com/problems/implement-rand10-using-rand7/
"""
import random


def rand7() -> int:
    return random.randint(1, 7)


def rand10(self) -> int:
    # 关键是构造出概率均匀分布的区间
    while True:
        row = rand7()
        col = rand7()
        # (row - 1) * 7 所得是数∈[0, 7, 14, 21, 28, 35, 42]的等概率分布
        # 每个数加上[1, 7]内的均匀分布，就变成了[1, 49]内的均匀分布
        idx = (row - 1) * 7 + col
        if idx <= 40:
            return 1 + (idx - 1) % 10
