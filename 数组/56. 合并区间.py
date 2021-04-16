"""
https://leetcode-cn.com/problems/merge-intervals/
按照区间的左端点排序，可以合并的区间是连续的
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        # 结果为空或结果的最后一个区间与该区间不重合
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        # 将结果最后一个区间的右端点改为较大的那一个
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result
