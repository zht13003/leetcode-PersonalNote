"""
https://leetcode-cn.com/problems/student-attendance-record-ii/
dp[i][j][k]为前i天，总计缺席j（0，1）次，结尾连续迟到k（0，1，2）次的数量
共6种情况：dp[i][0][0]、dp[i][1][0]、dp[i][0][1]...
"""

def checkRecord(n: int) -> int:
    MOD = 10 ** 9 + 7
    dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        # 如果今天出席，可以将连续迟到记录抹除，即将前一天所有k种情况的数量加起来
        for j in range(0, 2):
            for k in range(0, 3):
                dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

        # 如果今天缺席，需要前面天数的缺席次数为0，同时将连续迟到记录抹除
        for k in range(0, 3):
            dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

        # 如果今天迟到，且已连续迟到k次（k∈0，1，2），那么前一天一定连续迟到了k-1次，需要加上k-1次的数量
        for j in range(0, 2):
            for k in range(1, 3):
                dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD

    total = 0
    for j in range(0, 2):
        for k in range(0, 3):
            total += dp[n][j][k]
    return total % MOD