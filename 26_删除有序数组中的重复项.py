# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/1 10:45
# @Author : San_mao_liu
# @File : 26_删除有序数组中的重复项.py
# @Software: PyCharm

def remove_duplicates(nums):
    if not nums:
        return

    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 0
        else:
            dic[i] += 1

    keys = list(dic.keys())

    return len(keys)

nums = [1, 1, 2]

print(remove_duplicates(nums))
