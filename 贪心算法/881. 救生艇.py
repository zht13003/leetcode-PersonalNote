"""
https://leetcode-cn.com/problems/boats-to-save-people/
为了使船数最少，希望载两人的船尽可能地多
将体重排序，考虑最轻和最重的两个
最轻+最重>上限——最重只能单独分配一艘
最轻+最重<上限——说明最轻可以和任何人同乘。为了尽可能最大化利用空间，让最轻和最重分配在一起是最好的选择
"""
from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    result = 0
    people.sort()
    light, weight = 0, len(people) - 1
    while light <= weight:
        if people[light] + people[weight] > limit:
            weight -= 1
        else:
            light += 1
            weight -= 1
        result += 1
    return result