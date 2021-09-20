"""
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
300. 最长递增子序列的延申
设cnt[i]为以nums[i]为结尾的最长递增子序列的个数
"""
from typing import List


def findNumberOfLIS(nums: List[int]) -> int:
    n, max_len, ans = len(nums), 0, 0
    dp = [0] * n
    cnt = [0] * n
    for i, x in enumerate(nums):
        dp[i] = 1
        cnt[i] = 1
        for j in range(i):
            if x > nums[j]:
                # 转移方程：dp[i]=max(1 + dp[j], dp[i])
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]  # 重置计数
                # 状态i是由状态j转移过来的
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
        if dp[i] > max_len:
            max_len = dp[i]
            ans = cnt[i]  # 重置计数
        elif dp[i] == max_len:
            ans += cnt[i]
    return ans