"""
https://leetcode-cn.com/problems/count-numbers-with-unique-digits/
排列组合
"""
def countNumbersWithUniqueDigits(n: int) -> int:
    dp = [1, 10]
    for i in range(2, n + 1):
        if i > 10:
            return dp[10]
        temp = 9
        base = 9
        # 计算有多少个n位数，其各位数字不同。第一位有9种选择，第二位有9种，第三位有8种...
        for _ in range(2, i + 1):
            temp *= base
            base -= 1
        dp.append(dp[i - 1] + temp)
    return dp[n]


print(countNumbersWithUniqueDigits(4))