"""
https://leetcode-cn.com/problems/russian-doll-envelopes/
注意到，组合好的信封的长度序列和宽度序列都是递增序列
可以看作是两个300.最长递增子序列问题
由于两个组合的信封长度与宽度不能相同，因此采用以下方法
将信封按长度递增排序后，对于长度相同的信封，按照宽度递减排序，最后对宽度组成的数组求最长递增子序列
这样，在求宽度的递增子序列时，就会将那些具有相同长度的信封中宽度较大的跳过，选中宽度最小的那个
"""
from typing import List
from operator import itemgetter


def maxEnvelopes(envelopes: List[List[int]]) -> int:
    n = len(envelopes)
    envelopes.sort(key=itemgetter(0))
    i = 0
    while i < n - 1:
        if envelopes[i][0] == envelopes[i + 1][0]:
            flag = i
            for _ in range(i + 1, n):
                flag += 1
                if envelopes[i][0] != envelopes[flag][0]:
                    flag -= 1
                    break
            part = envelopes[i:flag + 1]
            part.sort(key=itemgetter(1), reverse=True)
            envelopes[i:flag + 1] = part
            i = flag
        i += 1
    height = []
    for i in range(n):
        height.append(envelopes[i][1])
    return lengthOfLIS(height)


# 同300.最长递增子序列最长递增子序列
def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


envelopes = [[2, 3], [5, 4], [6, 4], [6, 7], [5, 2], [1, 8]]
envelopes2 = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(maxEnvelopes(envelopes2))
