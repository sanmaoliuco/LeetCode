# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/2 20:02
# @Author : San_mao_liu
# @File : 122_买卖股票的最佳时机.py
# @Software: PyCharm


def maxProfit(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i - 1] < prices[i]:
            profit += prices[i] - prices[i - 1]

    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))























