"""
https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/
"""
from typing import List


def minSwaps(grid: List[List[int]]) -> int:
    n = len(grid)
    a = []
    # 记录每一行最后有多少个连续的0
    for i in range(n):
        count = 0
        for j in reversed(range(n)):
            if grid[i][j] == 0:
                count += 1
            else:
                break
        a.append(count)
    result = 0
    for i in range(n - 1):
        # 如果第i行最后0的个数满足要求，就跳过
        if a[i] >= n - i - 1:
            continue
        # 否则向下找到第一个满足要求的行并交换上来
        else:
            j = i
            for _ in range(j, n):
                if a[j] >= n - i - 1:
                    break
                j += 1
            if j == n:
                return -1
            while j > i:
                temp = a[j - 1]
                a[j - 1] = a[j]
                a[j] = temp
                result += 1
                j -= 1
    return result



print(10 ** 2)