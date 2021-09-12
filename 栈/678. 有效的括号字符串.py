"""
https://leetcode-cn.com/problems/valid-parenthesis-string/
"""

# 贪心算法，从左到右遍历一次使得)能够匹配(，从右到左遍历一次使得(能够匹配)
def checkValidString(s: str) -> bool:
    # 左括号的数量，星号数量
    left, star = 0, 0
    for i in s:
        if i == "(":
            left += 1
        if i == ")":
            left -= 1
        if i == "*":
            star += 1
        # 右括号数量大于左括号时，用一个星号代替
        if left < 0:
            star -= 1
            left += 1
        # 星号不够时，匹配失败
        if star < 0:
            return False

    right, star = 0, 0
    for i in reversed(s):
        if i == ")":
            right += 1
        if i == "(":
            right -= 1
        if i == "*":
            star += 1
        if right < 0:
            star -= 1
            left += 1
        if star < 0:
            return False
    return True

# 用两个栈，维护(的下标以及*的下标
def checkValidString2(s: str) -> bool:
    left, star = [], []
    for i in range(len(s)):
        if s[i] == "(":
            left.append(i)
        # 优先用(栈进行匹配，否则用*栈进行匹配
        if s[i] == ")":
            if len(left) == 0:
                if len(star) == 0:
                    return False
                else:
                    star.pop()
            else:
                left.pop()
        if s[i] == "*":
            star.append(i)
    # (的下标必须大于*的下标
    while len(left) != 0 and len(star) != 0:
        if left.pop() > star.pop():
            return False
    return len(left) == 0