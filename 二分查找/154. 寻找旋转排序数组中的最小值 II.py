"""
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
数组以最小值为分界点被分为两个递增的子数组
分界点的左侧元素都大于分界点，右侧元素都小于分界点
用二分查找，当中间点大于右端点时，说明中间点位于分界点的左侧
当中间点小于右端点时，说明中间点位于分界点的右侧
当中间点等于右端点时，假设其等于最小值，那么我们可以忽略右端点，因为可以用中间点代替
|       *
|     *
|   *
|            *
|  最小值-> *
|---------------------------
"""
from typing import List


def findMin(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        pivot = low + (high - low) // 2
        if nums[pivot] < nums[high]:
            high = pivot
        elif nums[pivot] > nums[high]:
            low = pivot + 1
        else:
            high -= 1
    return nums[low]