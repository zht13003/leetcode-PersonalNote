"""
https://leetcode-cn.com/problems/ipo/
每次在当前能够选择的项目内，选择利润最大的那个
"""

import heapq
from typing import List


def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    if w >= max(capital):
        return w + sum(heapq.nlargest(k, profits))

    n = len(profits)
    curr = 0
    arr = [(capital[i], profits[i]) for i in range(n)]
    # 按最小资本排序
    arr.sort(key=lambda x: x[0])

    pq = []
    for _ in range(k):
        # 将最小资本小于当前资本的项目都放进堆内
        while curr < n and arr[curr][0] <= w:
            heapq.heappush(pq, -arr[curr][1])
            curr += 1
        # 堆不为空时，将堆顶取出
        if pq:
            w -= heapq.heappop(pq)
        else:
            break
    return w