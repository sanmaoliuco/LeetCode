# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/14 8:21
# @Author : San_mao_liu
# @File : 路径数目.py
# @Software: PyCharm


# dp = [[0 for _ in range(5)] for _ in range(5)]
# print(dp)
def uniquePaths(m,n):
    row = m
    col = n

    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(col):
        dp[0][i] = 1
    for j in range(row):
        dp[j][0] = 1

    for j in range(1,row):
        for i in range(1,col):
            dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

    return dp[row-1][col-1]


def unique_Paths(m,n):
    res = 1
    x = n
    y = 1
    while x <= n + m - 2:
        res = res * x // y
        x += 1
        y += 1
    return res



# print(uniquePaths(3,7))
print(unique_Paths(3,7))


















