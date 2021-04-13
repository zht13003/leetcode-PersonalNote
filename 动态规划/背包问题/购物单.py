"""
https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey
可以看作是01背包问题的扩展版
对每个主件，有4个版本：不带附件、1个附件1、1个附件2、2个附件1附件2
dp[i][j]为前i个物品、预算为j的情况下的最大价值
w[i][k]为第i个物品在k情况下的价格，v[i][k]为第i个物品在k情况下的价值，k = 0, 1, 2, 3
dp[i][j] = max{dp[i - 1][j]                           ,不将该物品放入背包
              {max(dp[i - 1][j - w[i][k]] + v[i][k])  ,取4种情况中价值最高的放入背包
"""
'''
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
'''
import sys

n, m = map(int, sys.stdin.readline().split(' '))
primary, annex = {}, {}
for i in range(1, m + 1):
    x, y, z = map(int, sys.stdin.readline().split(' '))
    if z == 0:
        primary[i] = [x, y]
    else:
        if z in annex:
            annex[z].append([x, y])
        else:
            annex[z] = [[x, y]]

m = len(primary)
dp = [[0] * (n + 1) for _ in range(m + 1)]
# 第0个物品为空集
w, v =[[]], [[]]
for key in primary:
    w_temp, v_temp = [], []
    # 不加附件的情况
    w_temp.append(primary[key][0])
    v_temp.append(primary[key][0] * primary[key][1])
    # 加附件的情况
    if key in annex:
        w_temp.append(w_temp[0] + annex[key][0][0])
        v_temp.append(v_temp[0] + annex[key][0][0] * annex[key][0][1])
        # 加两个附件的情况
        if len(annex[key]) > 1:
            w_temp.append(w_temp[0]+annex[key][1][0])
            v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
            w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
for i in range(1, m + 1):
    for j in range(10, n + 1, 10):
        max_i = dp[i - 1][j]
        for k in range(len(w[i])):
            if j - w[i][k] >= 0:
                max_i = max(max_i, dp[i - 1][j - w[i][k]] + v[i][k])
        dp[i][j] = max_i
print(dp[m][n])