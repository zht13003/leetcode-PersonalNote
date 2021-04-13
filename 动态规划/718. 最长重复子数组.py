"""
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
与1143. 最长公共子序列 类似
"""
from typing import List

'''
记dp[i][j]为以nums1[i - 1]、nums2[j - 1]为结尾的公共子数组的长度
dp[i][j] = {dp[i - 1][j - 1] + 1   ,nums1[i - 1] == nums2[j - 1],可以放入公共子数组中
           {0                      ,否则,不能作为公共子数组
'''
def findLength(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    for i in range(1, m + 1):
        num1 = nums1[i - 1]
        for j in range(1, n + 1):
            num2 = nums2[j - 1]
            if num1 == num2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            if dp[i][j] > max_len:
                max_len = dp[i][j]
    return max_len

'''
滑动窗口
------------------
  1 2 3 2 1 
------------------
      3 2 1 4 7 8
------------------
'''
def findLength2(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    # 对于给定的滑动距离，计算相同位置上相同的子数组
    def max_length(start1: int, start2: int, length: int) -> int:
        ret = k = 0
        for i in range(length):
            if nums1[start1 + i] == nums2[start2 + i]:
                k += 1
                ret = max(ret, k)
            else:
                k = 0
        return ret
    ret = 0
    # length表示滑动后两数组重合部分的长度
    for i in range(m):
        length = min(n, m - i)
        ret = max(ret, max_length(i, 0, length))
    for i in range(n):
        length = min(m, n - i)
        ret = max(ret, max_length(0, i, length))
    return ret