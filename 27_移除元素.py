# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/18 10:01
# @Author : San_mao_liu
# @File : 27_移除元素.py
# @Software: PyCharm

def removeElement(nums,val):

    slow_index = 0
    for fast_index in range(len(nums)):
        if val != nums[fast_index]:
            nums[slow_index] = nums[fast_index]
            slow_index += 1

    return slow_index

def remove_element(nums,val):
    idx = 0
    for x in nums:
        if x != val:
            nums[idx] = x
            idx += 1
    return idx


nums = [1,2,2,3,4,5,2,5]
val = 2
# print(removeElement(nums,val))
print(remove_element(nums,val))








