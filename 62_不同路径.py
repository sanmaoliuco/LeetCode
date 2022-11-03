# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/13 8:58
# @Author : San_mao_liu
# @File : 62_不同路径.py
# @Software: PyCharm


def uniquePath(m,n):

    dp = [[1]*n for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):

            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


# print(uniquePath(3,7))

def unique_path(m,n):
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[-1]

print(unique_path(3, 5))


dp = [[1]*7] + [[1] + [0] * 6 for _ in range(2)]
print(dp)













