"""
https://leetcode-cn.com/problems/integer-break/
----------------------------
|----j----|-------i-j------|
|-------------i------------|
设dp[i]为长度为i的整数拆分得到的最大乘积
两层循环，j<i
dp[i]=max(dp[j], dp[i-j])
         长度为j  长度为i-j
"""


def integerBreak(n: int) -> int:
    if n < 2:
        return 0
    if n <= 3:
        return n - 1
    dp = [0] * (n + 1)
    for i in range(4):
        dp[i] = i
    for i in range(4, n + 1):
        maximum = 0
        # 由对称性，j只需遍历到整数的中央即可
        for j in range(1, int(i / 2) + 1):
            maximum = max(maximum, dp[j] * dp[i - j])
            dp[i] = maximum
    return dp[n]