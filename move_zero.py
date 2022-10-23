# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/2 9:05
# @Author : San_mao_liu
# @File : move_zero.py
# @Software: PyCharm

def move_zero(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]

            if i != j :
                nums[i] = 0

            j = j+1
    return nums

def moveZero(nums):
    for i in nums:
        if i == 0:
            nums.remove(0)
            nums.append(0)

    return nums



nums = [0,1,0,3,12]

# print(move_zero(nums))
print(moveZero(nums))








