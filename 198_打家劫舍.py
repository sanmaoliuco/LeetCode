# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/22 20:22
# @Author : San_mao_liu
# @File : 198_打家劫舍.py
# @Software: PyCharm


'''
a, 子问题
b，状态定义
c，dp方程
'''


def rob(nums):
    if nums == None or len(nums) == 0:
        return 0

    a = [[0,0] for _ in range(len(nums))]
    a[0][0] = 0
    a[0][1] = nums[0]

    for i in range(len(nums)):
        a[i][0] = max(a[i-1][0],a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]

    return max(a[len(nums) - 1][0],a[len(nums) - 1][1])

nums = [1,2,3,4]
print(rob(nums))


def rob_2(nums):
    if nums == None or len(nums) == 0:return 0
    if len(nums) == 1: return nums[0]
    n = len(nums)
    a = [[0] for _ in range(n)]
    a[0] = nums[0]
    a[1] = max(nums[0], nums[1])
    res = max(a[0], a[1])
    for i in range(2, n):
        a[i] = max(a[i-1], a[i-2] + nums[i])
        res = max(res, a[i])

    return res



def rob_3(nums):
    prev_max = 0
    curr_max = 0
    for x in nums:
        temp = curr_max
        curr_max = max(prev_max + x, curr_max)
        prev_max = temp

    return curr_max


nums1 = [2,3,2]
print(rob_3(nums))
print(rob_3(nums1))

# import math
# c = int(math.sqrt(5))
# print(c)
#
#
#
#
# a = [[0, 0]] * 4
# b = [[0, 0] for _ in range(len(nums))]
#
# print(a)
# print(b)










