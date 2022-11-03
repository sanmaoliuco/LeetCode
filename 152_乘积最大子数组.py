# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/31 9:36
# @Author : San_mao_liu
# @File : 152_乘积最大子数组.py
# @Software: PyCharm


def maxProduct(nums):
    mi = ma = res = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0: mi, ma  = ma, mi
        ma = max(nums[i], ma * nums[i])
        mi = min(nums[i], mi * nums[i])

        res = max(res, ma)

    return res

def max_pro(nums):
    ma = mi = res = nums[0]
    for i in range(1, len(nums)):
        m_a = ma
        m_i = mi
        ma = max(m_a* nums[i], max(nums[i], m_i*nums[i]))
        mi = min(m_i, nums[i], min(nums[i], m_a*nums[i]))
        res = max(res, ma)

    return res



nums = [2, 3, -2, 4]
nums_1 = [-2, 0, -1]
nums_2 = [-3, 2, -4]
# print(maxProduct(nums_2))
# print(maxProduct(nums))












