"""
https://leetcode-cn.com/problems/smallest-k-lcci/
"""
import heapq
from typing import List


def smallestK(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return list()
    # 初始堆为arr的前k个数，然后对arr剩下的数依次与堆顶的数比较，如果小于堆顶就把堆顶弹出，插入这个数
    # 最后整个堆就是由k个最小的数组成
    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    for i in range(k, len(arr)):
        if -hp[0] > arr[i]:
            heapq.heappop(hp)
            heapq.heappush(hp, -arr[i])
    ans = [-x for x in hp]
    return ans