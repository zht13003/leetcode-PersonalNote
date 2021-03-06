"""
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""
from typing import List

from 堆.大根堆 import *


def findKthLargest(nums: List[int], k: int) -> int:
    heapSize = len(nums)
    build_max_heap(nums)
    for i in range(heapSize - 1, heapSize - k, -1):
        # 将堆的根节点与最后一个节点交换
        swap(nums, 0, i)
        # 将堆的大小减一，即忽视掉刚刚被替换掉的根节点
        heapSize -= 1
        # 将堆重新化为大根堆
        max_heapify(nums, 0, heapSize)
    return nums[0]


val = [8, 7, 5, 1, 2, 9, 6, 3, 0]
print(findKthLargest(val, 1))
a = {}
