# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/20 8:38
# @Author : San_mao_liu
# @File : 213_打家劫舍.py
# @Software: PyCharm

def rob(nums):
    if nums == None or len(nums) == 0:
        return 0

    a = [[0, 0] for _ in range(len(nums))]
    a[0][0] = 0
    a[0][1] = nums[0]

    for i in range(len(nums)):
        a[i][0] = max(a[i - 1][0], a[i - 1][1])
        a[i][1] = a[i - 1][0] + nums[i]

    return max(a[len(nums) - 1][0], a[len(nums) - 1][1])


def rob_1(nums):
    if nums == None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    a = [[0, 0] for _ in range(len(nums))]
    res1 = res2 = 0
    for i in range(0, len(nums) - 1):
        a[0][0] = 0
        a[0][1] = nums[0]
        a[i][0] = max(a[i - 1][0], a[i - 1][1])
        a[i][1] = a[i-1][0] + nums[i]
        res1 = max(a[len(nums) - 2][0], a[len(nums) - 2][1])

    for i in range(1, len(nums)):
        a[1][0] = 0
        a[1][1] = nums[1]
        a[i][0] = max(a[i-1][0], a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]
        res2 = max(a[len(nums) - 1][0], a[len(nums) - 1][1])

    return max(res1, res2)

nums = [1,2,3]
print(rob_1(nums))




















