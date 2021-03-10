"""
https://leetcode-cn.com/problems/basic-calculator/
由于只有加减操作，可以将+-储存为sign
"""


def calculate(s: str) -> int:
    ops = [1]
    sign = 1

    ret = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] == '+':
            sign = ops[-1]
            i += 1
        elif s[i] == '-':
            sign = -ops[-1]
            i += 1
        elif s[i] == '(':
            ops.append(sign)
            i += 1
        elif s[i] == ')':
            ops.pop()
            i += 1
        else:
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            ret += num * sign
    return ret


print(calculate('2+(3-5)-(6-(6+4))'))