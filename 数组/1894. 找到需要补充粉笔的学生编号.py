"""
https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk/
前缀和+二分查找
"""
from typing import List


def chalkReplacer(chalk: List[int], k: int) -> int:
    n = len(chalk)
    dp = [0] * n
    dp[0] = chalk[0]
    for i in range(1, n):
        dp[i] += dp[i - 1] + chalk[i]
    k = k % dp[-1]

    left, right = 0, n - 1
    while left < right:
        mid = int((left + right) / 2)
        if dp[mid] <= k:
            left = mid + 1
        else:
            right = mid
    return left

print(chalkReplacer([1], 100000))