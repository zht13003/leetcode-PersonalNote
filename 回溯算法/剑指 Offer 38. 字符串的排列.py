"""
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
"""
from typing import List


def permutation(s: str) -> List[str]:
    c, res = list(s), []

    def dfs(x: int):
        # 递归终止条件，已经到达字符串的最后一个
        if x == len(c) - 1:
            res.append(''.join(c))
            return
        dic = set()
        for i in range(x, len(c)):
            # 若s中存在重复字符，需跳过
            if c[i] in dic:
                continue
            dic.add(c[i])
            # 通过字符的交换，固定处于x位置的字符
            c[i], c[x] = c[x], c[i]
            dfs(x + 1)
            # 还原字符串
            c[i], c[x] = c[x], c[i]

    dfs(0)
    return res


print(permutation("abcd"))
