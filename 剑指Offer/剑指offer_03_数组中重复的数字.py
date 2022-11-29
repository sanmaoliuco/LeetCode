# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/29 11:35
# @Author : San_mao_liu
# @File : 剑指offer_03_数组中重复的数字.py
# @Software: PyCharm

def findRepeatNumber(nums):
    dic = {}
    for num in nums:
        if num in dic: return num
        dic[num] = 0

    return -1

def find_repeat_number(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]: return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    return -1

def find_Repeat_Number(nums):
    s = set()

    for num in nums:
        if num in s:
            return num
        s.add(num)

    return -1


nums = [4, 3, 1, 9, 2, 5, 3]
# print(findRepeatNumber(nums))
# print(find_repeat_number(nums))
print(find_Repeat_Number(nums))





