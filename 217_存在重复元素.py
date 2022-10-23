# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/25 9:16
# @Author : San_mao_liu
# @File : 217_存在重复元素.py
# @Software: PyCharm

def containDuplicate(nums):
    if len(nums) <= 1:
        return False
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] :
            return True

    return False

nums = [1,2,3,4]

print(containDuplicate(nums))

def contain(nums):
    dic = {}.fromkeys(nums)
    print(dic)
    if len(nums) == len(dic):
        return False
    else:
        return True

print(contain(nums))

import collections
has_map = collections.defaultdict(int)

print(has_map)
for i in nums:
    has_map[i] += 1

print(has_map)