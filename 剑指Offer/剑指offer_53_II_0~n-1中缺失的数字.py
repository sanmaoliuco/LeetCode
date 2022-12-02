# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/2 11:37
# @Author : San_mao_liu
# @File : 剑指offer_53_II_0~n-1中缺失的数字.py
# @Software: PyCharm


def missingNumer(nums):

    if len(nums) == 1 and nums[0] == 0:
        return 1
    s = []
    for i in range(nums[-1]+1):
        s.append(i)

    return (set(s) ^ set(nums)).pop() if (set(s) ^ set(nums)) else len(nums)


def missing_number(nums):
    s = set(nums)

    for i in range(len(nums) + 1):
        if i not in s:
            return i

def missing_Number(nums):
    for i, num in enumerate(nums):
        if i != num:
            return i

    return len(nums)

def Missing_number(nums):
    i, j = 0, len(nums) - 1
    while i <= j:
        m = i + (j - i) // 2
        if nums[m] == m: i = m + 1
        else: j = m - 1
    return i

nums = [0, 1, 3]
# print(missingNumer(nums))
# print(missing_number(nums))
# print(missing_Number(nums))
print(Missing_number(nums))


