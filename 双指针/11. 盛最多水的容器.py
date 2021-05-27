"""
https://leetcode-cn.com/problems/container-with-most-water/
双指针，容量为边界中长度最小的那一个*底边长度
移动指针时，长度较小的那一边向里移动
"""
from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    result = -1
    while left < right:
        ans = min(height[left], height[right]) * (right - left)
        result = max(result, ans)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result