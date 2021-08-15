"""
https://leetcode-cn.com/problems/out-of-boundary-paths/
设dp[i][j][k]为移动i次、到达点(j,k)，存在的路径数
"""


def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    result = 0
    dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
    dp[0][startRow][startColumn] = 1
    for i in range(maxMove):
        for j in range(m):
            for k in range(n):
                # 点(j,k)能够到达
                if dp[i][j][k] > 0:
                    # 上下左右移动一步
                    for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                        # 移动后在范围内
                        if 0 <= j1 < m and 0 <= k1 < n:
                            # 发现dp[i][][]只会在计算dp[i+1][][]时用到，可以去掉dp[i]这个维度
                            # 做法是在最外层循环的开头，新建dpNew[m][n]，代替dp[i+1][m][n]
                            dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % (10 ** 9 + 7)
                        # 出界，记录结果
                        else:
                            result = (result + dp[i][j][k]) % (10 ** 9 + 7)
    return result


print(findPaths(2, 2, 2, 0, 0))
