"""
https://leetcode-cn.com/problems/palindrome-partitioning/
要求解所有可能的结果，考虑使用回溯算法
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    n = len(s)
    '''
    用动态规划来记录s的子串s[i:j]是否是回文，相比直接判断减小了时间复杂度
    dp[i][j]表示s[i:j]是否是回文
    动态转移方程为dp[i][j] = {True                       ,  i >= j
                          {dp[i+1][j-1] and s[i]==s[j],  i < j
    即，当子串为空串或单字符，或者，子串向中间收缩一格的子串为回文，且子串的两端字符相同时，可以构成回文
    '''
    dp = [[True] * n for _ in range(n)]
    # 用双指针，由s的两端向内收缩，判断s[i:j]是否为回文
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

    ret = list()
    ans = list()

    # 回溯搜索，当搜索到字符串末尾时停止
    def dfs(i: int):
        if i == n:
            ret.append(ans[:])
            return

        for j in range(i, n):
            if dp[i][j]:
                ans.append(s[i:j + 1])
                dfs(j + 1)
                ans.pop()

    dfs(0)
    return ret