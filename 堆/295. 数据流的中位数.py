"""
https://leetcode-cn.com/problems/find-median-from-data-stream/
用一个大根堆和一个小根堆来维护数据
大根堆存储小于等于中位数的数，小根堆存储大于中位数的数
当两堆数量相同时，中位数为两堆堆头的平均数，否则为大根堆的堆头
添加一个数时，小于大根堆堆头，则添加到大根堆。大于小根堆堆头，则添加到小根堆
同时需要维护大根堆的数量等于小根堆的数量或小根堆的数量+1
通过将大根堆的堆头加入小根堆，或小根堆的堆头加入大根堆
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2