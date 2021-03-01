"""
https://leetcode-cn.com/problems/longest-increasing-subsequence/
dp[i]为前i个元素中，“”以第i个元素为结尾“”的最长递增子序列的长度
状态转移需要两层循环，外层i对数组中n个元素循环，内层j对0~i个元素循环
状态转移方程为在nums[i] > nums[j]，即nums[i]能放到以nums[j]的递增子序列的结尾的条件下：
dp[i]=max(1 + dp[j],  ————将nums[i]放入
          dp[i]       ————不将nums[i]放入
"""
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if not nums: return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18, 102]
print(lengthOfLIS(nums))
