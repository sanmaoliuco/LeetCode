# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/24 10:35
# @Author : San_mao_liu
# @File : maxProfit.py
# @Software: PyCharm

# def maxProfit(prices):
#     m = len(prices)
#     dp = [0] * m
#
#     min_price = prices[0]
#
#     for i in range(1, m):
#         min_price = min(min_price, prices[i])
#         dp[i] = max(dp[i - 1], prices[i] - min_price)
#
#     return dp[m - 1]
#
#
# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))

def Floor_DP(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return (Floor_DP(n-1) + Floor_DP(n - 2))


print(Floor_DP(3))























