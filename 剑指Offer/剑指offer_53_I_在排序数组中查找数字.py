# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/2 11:29
# @Author : San_mao_liu
# @File : 剑指offer_53_I_在排序数组中查找数字.py
# @Software: PyCharm

from collections import Counter
def search(nums, target):
    s = Counter(nums)
    if target in s:
        return s[target]
    else:
        return 0

nums = [5,7,7,8,8,10]
target = 8
print(search(nums, target))




