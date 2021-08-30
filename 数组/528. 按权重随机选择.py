"""
https://leetcode-cn.com/problems/random-pick-with-weight/
可以假设一个长度为sum(w)的数组，分为len(w)段，第i段的长度为w[i]
如w=[3,1,2,4]
|---3---|-1-|--2--|----4----|
0       3   4     6         10
设w的前缀和数组为pre[i]，则上图数组的左端点为pre[i]-w[i]，右端点为pre[i]
随机生成一个数x，求x落在哪个区间，即满足pre[i]-w[i]<=x<=pre[i]
由于pre[i]递增，只需要找到第一个满足x<=pre[i]即可，可用二分查找
"""
import random
from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)
