"""
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
dp[j]代表以s[j]为结尾的最长不重复子串的长度
设s[i]为s[j]左边距离最近的相同字符
当i < 0，即s[j]左边没有相同字符时，dp[j]可以加入进dp[j - 1]中，即dp[j] = dp[j - 1] + 1
当dp[j - 1] < j - i，即s[i]位于以s[j - 1]结尾的子字符串之外，表明dp[j]可以加入进dp[j - 1]中，即dp[j] = dp[j - 1] + 1
当dp[j - 1] >= j - i，即s[i]位于以s[j - 1]结尾的子字符串之内，则以目标字符串为s[i]开始、s[j]结束，长度为j - i
考虑到dp[j]只与dp[j - 1]相关，只用一个变量tmp储存dp，并取res和tmp中较大者为结果
用一个字典dic记录各字符最后一次出现的索引
"""
def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    res = tmp = 0
    for j in range(len(s)):
        # 先获取再记入字典中，此时s[i]就是离s[j]最近的相同字符
        i = dic.get(s[j], -1)
        dic[s[j]] = j
        tmp = tmp + 1 if tmp < j - i else j - i
        res = max(res, tmp)
    return res


s = "abccdeffg"
print(lengthOfLongestSubstring(s))