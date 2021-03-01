# 给定n个不同长度的木棍，将木棍切割出至少k个、且长度相同为m的木棍。已知k，求m的最大值
# 输入n， k， [n个木棍各自的长度]，输出max(m)
from typing import List


# 暴力
def method_1(n: int, k: int, stick: List[int]):
    max_v = max(stick)
    res = 0
    m = 1
    # 切割长度为[1,max_v]
    while m <= max_v:
        cut = 0
        # 对每一个木棍遍历，计算能切割出长度为m的子木棍的个数cut
        for i in range(n):
            cut += int(stick[i] / m)
        # 如果切割个数符合要求（>=k），则记录长度
        if cut >= k:
            res = max([res, m])
        m += 1
    return res


# 二分查找
# 因为最后结果m在[1, max_v]之间，可以用二分查找，时间复杂度为O(nlog(maxstick))
def method_2(n: int, k: int, stick: List[int]):
    l = 1
    r = max(stick)
    while l < r:
        mid = int((l + r + 1) / 2)
        if check(mid, stick) >= k:
            l = mid
        else:
            r = mid - 1
    return l


def check(mid: int, stick: List[int]):
    res = 0
    for i in range(len(stick)):
        res += int(stick[i] / mid)
    return res


print(method_2(5, 2, [4, 7, 2, 10, 5]))
