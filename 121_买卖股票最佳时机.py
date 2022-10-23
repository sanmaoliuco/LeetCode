# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/9 9:56
# @Author : San_mao_liu
# @File : 121_买卖股票最佳时机.py
# @Software: PyCharm

def maxProfit(prices):
    maxprofit = 0

    minprice = prices[0]
    for i in range(len(prices)):
        # for j in range(i, len(prices)):
        #     if prices[i + 1] > prices[i]:
        #         maxprofit = max(maxprofit, prices[j] - prices[i])
        minprice = minprice if prices[i] > minprice else prices[i]
        maxprofit = max(maxprofit, prices[i] - minprice)

    return maxprofit


# prices = [7, 6, 4, 3, 1]
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

