# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/17 8:41
# @Author : San_mao_liu
# @File : 120_三角形最小路径和.py
# @Software: PyCharm

# 直接复用triangle

def minimumTotal(triangle):
    if not triangle:
        return

    for i in range(len(triangle) - 2,-1, -1):   # 从倒数第二行往上DP    DP数组就是原数组
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])

    return triangle[0][0]

triangle = [[2],
            [3,4],
            [1,4,5],
            [5,4,6,1]]



def min_mum(triangle):
    f = [0] * (len(triangle) + 1)
    for row in range(len(triangle) - 1, -1,-1):
        for i in range(len(triangle[row])):
            f[i] = triangle[row][i] + min(f[i],f[i+1])
    return f[0]

print(min_mum(triangle))

# print(minimumTotal(triangle))
















