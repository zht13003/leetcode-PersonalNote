"""
https://leetcode-cn.com/problems/word-search/
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    pathLength = 0

    def helper(row: int, col: int, pathLength: int):
        # 所有字符已经在矩阵上找到合适的位置
        if pathLength == len(word):
            return True
        hasPath = False
        # 该位置上矩阵的字符等于目标字符，且没有被访问过
        if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[pathLength] and not \
                visited[row][col]:
            # 匹配word的下一个字符
            pathLength += 1
            visited[row][col] = True
            # 向四周进行搜索
            hasPath = helper(row, col - 1, pathLength) or helper(row - 1, col, pathLength) or \
                      helper(row, col + 1, pathLength) or helper(row + 1, col, pathLength)
            # 四周没有匹配的字符，回到word的前一个字符
            if not hasPath:
                pathLength -= 1
                visited[row][col] = False
        return hasPath

    for i in range(rows):
        for j in range(cols):
            if helper(i, j, pathLength):
                return True
    return False
