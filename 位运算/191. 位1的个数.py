"""
https://leetcode-cn.com/problems/number-of-1-bits/
一种解法：n与1进行与运算，如果结果为1，说明n的最右边为1，之后n右移一位
另一种解法：
n      : 1 0 1 0 1 0 0 0
n-1    : 1 0 1 0 0 1 1 1
n&(n-1): 1 0 1 0 0 0 0 0
即n&(n-1)是把n的最右边的1变为0
"""


def hammingWeight(n: int) -> int:
    res = 0
    while n != 0:
        res += 1
        n = (n - 1) & n
    return res