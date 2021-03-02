"""
https://leetcode-cn.com/problems/range-sum-query-2d-immutable/
与303题相似，用dp[i][j]储存左上坐标为[0,0]、右下坐标为[i,j]的矩阵元素和
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        if row == 0:
            return
        column = len(matrix[0])
        dp = [[0] * column for _ in range(row)]
        dp[0][0] = matrix[0][0]
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]
        for i in range(1, column):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]
        for i in range(1, row):
            for j in range(1, column):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]
        # 在dp矩阵外部插入一圈0，避免之后的复杂判断
        dp.insert(0, [0] * len(dp[0]))
        for i in range(len(dp)):
            dp[i].insert(0, 0)
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        return dp[row2 + 1][col2 + 1] - dp[row2 + 1][col1] - dp[row1][col2 + 1] + dp[row1][col1]


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
res = NumMatrix(matrix)
print(res.sumRegion(1, 1, 2, 3))
