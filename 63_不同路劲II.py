# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/13 9:37
# @Author : San_mao_liu
# @File : 63_不同路劲II.py
# @Software: PyCharm


def uniquePathWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m) ]

    for i in range(m):
        if obstacleGrid[i][0] == 1:break   # 第一列
        dp[i][0] = 1
    for j in range(n):     # 第一行
        if obstacleGrid[0][j] == 1:break
        dp[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


obstacle = [[0,0,0],[0,1,0],[0,0,0]]
# print(uniquePathWithObstacles(obstacle))


def uniquePath_WithObstacles(obstacleGrid):
    m,n = len(obstacleGrid),len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 0:# 元素是否为障碍物
                if i == j == 0:
                    dp[i][j] = 1
                    continue

                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]


    return dp[-1][-1]

print(uniquePath_WithObstacles(obstacle))




