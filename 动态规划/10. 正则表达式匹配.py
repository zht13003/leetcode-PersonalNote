"""
https://leetcode-cn.com/problems/regular-expression-matching/
问题可以缩小为前i个字符是否能匹配前j个模式，使用动态规划
dp[i][j]为前i个字符是否能匹配前j个模式
转移方程为：
    当p[j]==字母或.时，需要s[i]==p[j]，即dp[i][j]={dp[i-1][j-1],  s[i]=p[j]
                                              {False,         s[i]!=p[j]
    当p[j]==*时，即a*可以匹配零次或多次a：
                                匹配零次，即去掉这个匹配，dp[i][j]=dp[i][j-2]
                                匹配多次，即当s[i]==p[j-1]时，仍用这个规则匹配，dp[i][j]=dp[i-1][j]
"""

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    def match(i: int, j: int) -> bool:
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # 匹配零次，不管什么条件都满足
                dp[i][j] = dp[i][j - 2]
                # 如果s[i]==p[j-1]，要么匹配零次，即与上一行结果相等，要么匹配多次，即dp[i][j]=dp[i-1][j]
                if match(i, j - 1):
                    dp[i][j] |= dp[i - 1][j]
            else:
                if match(i, j):
                    dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]
