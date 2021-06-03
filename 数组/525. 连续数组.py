"""
https://leetcode-cn.com/problems/contiguous-array/
若将数组中的0变为-1，问题可以转化为寻找最长的连续子数组，使其和为0
用一个哈希表map{counter:i}表示数组的前i个元素之和counter
 1 1 1 -1 -1 1 1 -1 -1
|----------|
     ^
  前缀和为1
|---------------------|
           ^
        前缀和为1
则：         |---------|
                 ^
              前缀和为0
找到两个前缀和相等的位置，它们之间的差的前缀和即为0
"""
from typing import List


def finMaxLength(nums: List[int]) -> int:
    maxLength = 0
    map_counter_to_index = {0: -1}
    counter = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            counter += 1
        else:
            counter -= 1
        if counter in map_counter_to_index:
            prevIndex = map_counter_to_index[counter]
            maxLength = max(maxLength, i - prevIndex)
        else:
            map_counter_to_index[counter] = i
    return maxLength
