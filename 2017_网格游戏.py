# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/7 9:41
# @Author : San_mao_liu
# @File : 2017_网格游戏.py
# @Software: PyCharm

def gridGame(grid):

    n = len(grid[0])
    r2 , r1 = [0] * n,[0]*n

    for i in range(n-1,0,-1):
        r1[i-1] = r1[i] + grid[0][i]
    for i in range(n - 1):
        r2[i+1] = r2[i] + grid[1][i]

    res = float('inf')

    for i in range(n):
        res = min(res,max(r1[i],r2[i]))

    return res

    # n = len(grid[0])
    # r1, r2 = [0] * n, [0] * n
    # for i in range(n - 1, 0, -1): r1[i - 1] = r1[i] + grid[0][i]
    # for i in range(n - 1): r2[i + 1] = r2[i] + grid[1][i]
    # res = float('inf')
    # for i in range(n): res = min(res, max(r1[i], r2[i]))
    # return res



grid = [[2,5,4],[1,5,1]]
print(gridGame(grid))





















