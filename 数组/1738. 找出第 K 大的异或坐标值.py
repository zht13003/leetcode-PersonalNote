"""
https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/
注意，x ^ y ^ y = x
"""
import operator
import random
from typing import Callable, List


def kthLargestValue(matrix: List[List[int]], k: int) -> int:
    m, n = len(matrix), len(matrix[0])
    pre = [[0] * (n + 1) for _ in range(m + 1)]
    results = list()
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
            results.append(pre[i][j])

    def nth_element(left: int, kth: int, right: int, op: Callable[[int, int], bool]):
        if left == right:
            return

        pivot = random.randint(left, right)
        results[pivot], results[right] = results[right], results[pivot]

        # 三路划分（three-way partition）
        sepl = sepr = left - 1
        for i in range(left, right + 1):
            if op(results[i], results[right]):
                sepr += 1
                if sepr != i:
                    results[sepr], results[i] = results[i], results[sepr]
                sepl += 1
                if sepl != sepr:
                    results[sepl], results[sepr] = results[sepr], results[sepl]
            elif results[i] == results[right]:
                sepr += 1
                if sepr != i:
                    results[sepr], results[i] = results[i], results[sepr]

        if sepl < left + kth <= sepr:
            return
        elif left + kth <= sepl:
            nth_element(left, kth, sepl, op)
        else:
            nth_element(sepr + 1, kth - (sepr - left + 1), right, op)

    nth_element(0, k - 1, len(results) - 1, operator.gt)
    return results[k - 1]