"""
https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/
"""
from typing import List


# 双指针
def findLongestWord(s: str, dictionary: List[str]) -> str:
    # 将字典按字符串长度倒序、字典序排列
    dictionary.sort(key=lambda x: (-len(x), x))
    for word in dictionary:
        i, j = 0, 0
        # 用双指针检查word是否是s的子序列
        while i < len(word) and j < len(s):
            if word[i] != s[j]:
                j += 1
            else:
                j += 1
                i += 1
        if i == len(word):
            return word
    return ""


'''
可以用动态规划对字符串进行预处理，代替使用双指针查找
dp[i][j]为从位置i开始第一次出现字符j的位置，j∈[1,26]
对s进行倒序遍历，dp[i][j] = {i,             s[i] == j
                          dp[i + 1][j],  s[i] != j
此外，添加一组边界dp[len(s)][] = len(s)，若dp[i][j] == len(s)，表示从i开始不存在字符j
'''


def findLongestWord2(s: str, dictionary: List[str]) -> str:
    m = len(s)
    dp = [[0] * 26 for _ in range(m)]
    dp.append([m] * 26)

    for i in range(m - 1, -1, -1):
        for j in range(26):
            if ord(s[i]) == j + 97:
                dp[i][j] = i
            else:
                dp[i][j] = dp[i + 1][j]

    dictionary.sort(key=lambda x: (-len(x), x))
    for word in dictionary:
        match = True
        j = 0
        for i in word:
            # j后不存在该字符
            if dp[j][ord(i) - 97] == m:
                match = False
                break
            # j后存在该字符，对s的下一个字符进行匹配
            j = dp[j][ord(i) - 97] + 1
        if match:
            return word
    return ""
