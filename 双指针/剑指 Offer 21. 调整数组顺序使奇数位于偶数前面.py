"""
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
"""
from typing import List


def exchange(nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []
    end = n - 1
    begin = 0
    while begin < end:
        while begin < end and nums[begin] % 2 != 0:
            begin += 1
        while begin < end and nums[end] % 2 == 0:
            end -= 1
        if begin < end:
            temp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = temp
    return nums