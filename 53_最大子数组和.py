# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/31 9:14
# @Author : San_mao_liu
# @File : 53_最大子数组和.py
# @Software: PyCharm


"""
1、暴力 n^2
2、DP:
    a、分治(子问题)
    b、状态数组定义
    c、DP方程
"""

def maxSubArray(nums):
    dp = nums
    for i in range(1,len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])

    print(dp)
    return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))








