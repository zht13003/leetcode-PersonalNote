"""
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
"""


def movingCount(m: int, n: int, k: int) -> int:
    visited = [[False] * n for _ in range(m)]

    # 统计数位之和
    def digitSum(number: int) -> int:
        sum = 0
        while number > 0:
            sum += number % 10
            number = int(number / 10)
        return sum

    # 检查格子是否符合要求
    def check(row: int, col: int) -> bool:
        if 0 <= row < m and 0 <= col < n and digitSum(row) + digitSum(col) <= k and not visited[row][col]:
            return True
        return False

    def helper(row: int, col: int) -> int:
        count = 0
        if check(row, col):
            visited[row][col] = True
            # 可以省略向下和向左的搜索
            count = 1 + helper(row + 1, col) + helper(row, col + 1)
        return count

    result = helper(0, 0)
    return result