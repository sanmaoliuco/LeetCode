# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/23 9:15
# @Author : San_mao_liu
# @File : 746_使用最小花费爬楼梯.py
# @Software: PyCharm

def minCostClimbingStairs(cost):

    dp = [0 for _ in range(len(cost))]

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2,len(cost)):
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i]

    return min(dp[-1], dp[-2])

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost1 = [10, 15, 20]
print(minCostClimbingStairs(cost))
print(minCostClimbingStairs(cost1))












