"""
https://leetcode-cn.com/problems/counting-bits/
对于奇数，比前一个偶数多一个1，如5:101，4:100
对于偶数，1的个数等于除以2后的那个数，如6:110，3:11
因为最低位是0，除以2是右移一位，1的个数不变
"""
from typing import List


def countBits(num: int) -> List[int]:
    dp = [0] * (num + 1)
    for i in range(1, num + 1):
        if i % 2 == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[int(i / 2)]
    return dp


print(countBits(5))