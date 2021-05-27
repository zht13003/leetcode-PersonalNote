"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
二分法查找第一个target的位置及第一个大于target的位置-1
"""
from typing import List


def binary(nums: List[int], target: int, mode: bool) -> int:
    left = 0
    right = len(nums) - 1
    result = len(nums)
    while left <= right:
        mid = int((right + left) / 2)
        if nums[mid] > target or (mode and nums[mid] >= target):
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result


def searchRange(nums: List[int], target: int) -> List[int]:
    left = binary(nums, target, True)
    right = binary(nums, target, False) - 1
    if left <= right < len(nums) and nums[left] == target and nums[right] == target:
        return [left, right]
    else:
        return [-1, -1]
