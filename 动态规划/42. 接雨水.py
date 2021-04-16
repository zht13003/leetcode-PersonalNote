"""
https://leetcode-cn.com/problems/trapping-rain-water/
下标为i的地方能承接的雨水为左侧最大高度、右侧最大高度中的较小者，减去该处的高度
用left_max[i]记录下标为i处左侧高度的最大值，right_max为右侧
"""
from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[n - 1] = height[n - 1]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    result = 0
    for i in range(n):
        result += min(left_max[i], right_max[i]) - height[i]
    return result