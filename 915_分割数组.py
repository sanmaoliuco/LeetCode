# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/24 17:04
# @Author : San_mao_liu
# @File : 915_分割数组.py
# @Software: PyCharm


def partition_Disjoint(nums):
    # nums.sort()
    # print(nums)

    n = len(nums)
    cur_max = left_max = nums[0]
    left_pos = 0
    for i in range(1, n - 1):
        cur_max = max(cur_max, nums[i])
        if left_max > nums[i]:
            left_max, left_pos = cur_max, i
    return left_pos + 1


def partition_Dis(nums):
    left_max = right_max = nums[0]
    par_id = 0
    for i in range(1,len(nums)):
        right_max = max(right_max,nums[i])
        if nums[i] < left_max:
            left_max = right_max
            par_id = i

    return par_id + 1



nums = [8,6,5,0,3,]
# print(partition_Dis(nums))
# print(partition_Disjoint(nums))



















