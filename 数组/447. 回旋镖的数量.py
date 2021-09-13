"""
https://leetcode-cn.com/problems/number-of-boomerangs/
求出距离点p的距离相同的点p1、p2、p3...根据点的数量排列组合
"""
from collections import defaultdict
from typing import List


def numberOfBoomerangs(points: List[List[int]]) -> int:
    ans = 0
    for p1 in points:
        # key：距离点p1的长度，value：该距离长度的点的数量
        dic = defaultdict(int)
        for p2 in points:
            length = (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
            dic[length] += 1
        for i in dic.values():
            ans += i * (i - 1)
    return ans