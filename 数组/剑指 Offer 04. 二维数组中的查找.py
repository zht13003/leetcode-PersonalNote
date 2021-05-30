"""
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
从矩阵的右上角开始搜索，如果大于目标则左移，如果小于目标则下移
"""
from typing import List


def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    if rows == 0:
        return False
    cols = len(matrix[0])
    if rows > 0 and cols > 0:
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
    return False