"""
https://leetcode-cn.com/problems/beautiful-arrangement/
"""
from collections import defaultdict


def countArrangement(n: int) -> int:
    # 预先记录第i个位置上能够放置的整数
    match = defaultdict(list)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i % j == 0 or j % i == 0:
                match[i].append(j)
    num = 0
    vis = set()

    # 在第index个位置上进行放置
    def backtrack(index: int) -> None:
        # 放置到了末尾，退出
        if index == n + 1:
            nonlocal num
            num += 1
            return
        # 遍历每一个能放置在index位置上的数，如果这个数没有用过（不在vis中），就添加到vis中并递归放置下一个数，最后清空vis
        for x in match[index]:
            if x not in vis:
                vis.add(x)
                backtrack(index + 1)
                vis.discard(x)

    backtrack(1)
    return num