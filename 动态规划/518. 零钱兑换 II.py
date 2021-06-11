"""
https://leetcode-cn.com/problems/coin-change-2/
设dp[amount]是凑成amount金额的硬币组合数
可以看作是爬楼梯问题（70. 爬楼梯）的扩展
即有coins[0]、coins[1]。。。种爬楼梯的方法
"""
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    # 对于一个面值为coin的硬币，当coin <= i <= amount时，如果存在一种总额为i - coin的组合
    # 则可以将coin加入，形成一个组合
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]