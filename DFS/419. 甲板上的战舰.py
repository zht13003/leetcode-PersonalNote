"""
https://leetcode-cn.com/problems/battleships-in-a-board/
"""
from typing import List

# 搜索战舰头，它的左边和上面必定为空
def countBattleships(board: List[List[str]]) -> int:
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') \
                    and (j == 0 or board[i][j - 1] == '.'):
                count += 1
    return count

# DFS，每找到一个战舰进行计数，将其相邻的X改为.
def countBattleships2(board: List[List[str]]) -> int:
    count = 0
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'X':
                count += 1
                board[i][j] = '.'
                a = i + 1
                b = j
                while a < row and board[a][b] == 'X':
                    board[a][b] = '.'
                    a += 1
                a = i
                b = j + 1
                while b < col and board[a][b] == 'X':
                    board[a][b] = '.'
                    b += 1
    return count


board = [['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]
print(countBattleships2(board))
