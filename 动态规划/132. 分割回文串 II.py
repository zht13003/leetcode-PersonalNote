"""
https://leetcode-cn.com/problems/palindrome-partitioning-ii/
与131.分割回文串对比，求解的是最小分割次数，考虑使用动态规划
dp[i]为s[0:i]中分割回文串的最小次数，需要枚举[0,i]内的子串[0,j]
动态转移方程为dp[i] = min(dp[j]) + 1 , 当且仅当s[j + 1:i]为回文串，即状态可以由j到i，增加一次分割次数
判断子串是否为回文，同131.分割回文串，使用动态规划
"""


def minCut(s: str) -> int:
    n = len(s)
    dp = [[True] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

    f = [float("inf")] * n
    for i in range(n):
        # 若s[0:i]为回文，不需要切割
        if dp[0][i]:
            f[i] = 0
        else:
            for j in range(i):
                if dp[j + 1][i]:
                    f[i] = min(f[i], f[j] + 1)

    return f[n - 1]


