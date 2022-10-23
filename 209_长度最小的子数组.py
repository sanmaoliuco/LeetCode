# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/12 9:58
# @Author : San_mao_liu
# @File : 209_长度最小的子数组.py
# @Software: PyCharm


def minSubArrayLen(target, nums):
    if not nums or len(nums) == 0:
        return 0

    res = []

    # m = len(nums)

    re = []
    for i in nums:
        re.append(i)
        if sum(re) >= target:
            res.append(re)
            re = []

    return min(len(i) for i in res)



target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))










