# https://leetcode-cn.com/problems/range-sum-query-immutable/
# 求一个数组中从索引i到索引j的数字之和，且求和方法会调用很多次，需要该方法的时间复杂度为O(1)
# 考虑使用动态规划中的dp数组储存数组的前i项和，则求和结果为dp[j + 1] - dp[i]
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        _dp = []
        if len(nums) == 0:
            return
        for i in range(len(nums) + 1):
            _dp.append(sum(nums[0:i]))
        self.dp = _dp

    def sumRange(self, i: int, j: int) -> int:
        _dp = self.dp
        if i == 0:
            return _dp[j + 1]
        else:
            return _dp[j + 1] - _dp[i]


obj = NumArray([1, 2, 3, 4, 5])
param_1 = obj.sumRange(0, 1)
print(param_1)