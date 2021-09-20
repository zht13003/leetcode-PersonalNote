"""
https://leetcode-cn.com/problems/2-keys-keyboard/
设dp[i]为复制i个字符所需的最小步骤数
想要达到i个字符，需要在有j个字符后复制n次，且j为i的因数
则dp[i] = min(dp[i],
              dp[j] + i // j)，j∈[1, √i]
"""


def minSteps(n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float("inf")
        j = 1
        while j * j <= i:
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)
            j += 1
    return dp[n]