# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/14 8:40
# @Author : San_mao_liu
# @File : 64_最小路径和.py
# @Software: PyCharm

def minPathSum(grid):
    if grid is  None:
        return

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1,m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1,n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

    return dp[-1][-1]

def min_pathSum(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==j == 0 : continue
            elif i == 0 :
                grid[0][j] += grid[0][j-1]
            elif j == 0:
                grid[i][0] += grid[i-1][0]

            else:
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])

    return grid[-1][-1]




grid = [[1,3,1],[1,5,1],[4,2,1]]

print(minPathSum(grid))
print(min_pathSum(grid))
















