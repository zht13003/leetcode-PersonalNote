"""
https://leetcode-cn.com/problems/number-of-islands/
"""
from typing import List

# 将所有相邻的1改为0
def dfs(grid, r, c):
    grid[r][c] = 0
    nr, nc = len(grid), len(grid[0])
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
            dfs(grid, x, y)


def numIslands(grid: List[List[str]]) -> int:
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])

    num_islands = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == "1":
                num_islands += 1
                dfs(grid, r, c)

    return num_islands
