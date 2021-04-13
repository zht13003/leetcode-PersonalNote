"""
https://leetcode-cn.com/problems/longest-common-subsequence/
与718.最长重复子数组类似
dp[i][j]表示text1[:i]、text2[:j]的最长重复子序列长度
dp[i][j] = {dp[i - 1][j - 1] + 1             ,text1[i - 1] == text2[j - 1],可以放入公共子序列中
           {max(dp[i - 1][j], dp[i][j - 1])  ,否则,取text1或text2的上一个状态中最大的那个
"""
from typing import List


def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    for i in range(1, m + 1):
        t1 = text1[i - 1]
        for j in range(1, n + 1):
            t2 = text2[j - 1]
            if t1 == t2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            max_len = dp[i][j] if dp[i][j] > max_len else max_len
    return max_len


# 返回对应的最长公共子序列
def get_result(dp: List[List[int]], text1: str, text2: str) -> str:
    m = len(text1)
    n = len(text2)
    result = []
    # 根据状态方程进行逆推
    while m > 0 and n > 0:
        # 对应状态方程第一项
        if text1[m - 1] == text2[n - 1]:
            result.append(text1[m - 1])
            m -= 1
            n -= 1
        # 对应状态方程第二项
        else:
            if dp[m][n - 1] > dp[m - 1][n]:
                n -= 1
            elif dp[m][n - 1] < dp[m - 1][n]:
                m -= 1
            elif dp[m][n - 1] == dp[m - 1][n]:
                n -= 1
    ret = ""
    for i in reversed(range(len(result))):
        ret += result[i]
    if ret == "":
        return "-1"
    else:
        return ret