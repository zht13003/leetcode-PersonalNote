"""
https://leetcode-cn.com/problems/ones-and-zeroes/
可以视为两个背包问题，容量分别为能够使用的0和1的个数，字符串为装入背包的物品
dp[m][n]表示使用m个0、n个1能够组成的字符串个数，初始化为0
动态转移方程为dp[i][j]=max(1 + dp[i - 组合该字符串用掉的0个数][j - 组合该字符串用掉的1个数],  ————将该字符串装入背包
                       dp[i][j]                                                    ————不将该字符串装入背包
"""
from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    # 计算组合num字符串所需要的0和1的个数
    def cont(num):
        a = b = 0
        for i in range(len(num)):
            if int(num[i]) == 0:
                a += 1
            else:
                b += 1
        return [a, b]

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 对每个字符串遍历
    for i in strs:
        count = cont(i)
        # 性质是使用背包容量的背包问题，因此用逆序遍历
        for a in range(m, count[0] - 1, -1):
            for b in range(n, count[1] - 1, -1):
                dp[a][b] = max(1 + dp[a - count[0]][b - count[1]], dp[a][b])
    return dp[m][n]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))