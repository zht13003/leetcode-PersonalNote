"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
数组元素的索引和值是一对多的关系
可以通过扫描数组，将一个元素替换到索引=值的位置。这样遇到重复元素时，想要将其替换时会遇到该处索引已有值，可以看作是哈希冲突
"""
from typing import List


def findRepeatNumber(nums: List[int]) -> int:
    for i in range(len(nums)):
        # 一直替换，直到索引=值
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp