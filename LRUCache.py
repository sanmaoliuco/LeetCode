# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/9 8:48
# @Author : San_mao_liu
# @File : LRUCache.py
# @Software: PyCharm


'''
Cache 缓存

LRU Cache
两个要素：大小、替换策略
Hash Table + Double LinkedList

O(1)查询
O(1)修改、更新
 
'''

s1 = 'Please input your name!!'
s2 = 'put'

a = "*".join('python')
b = "|".join(['hello','python'])

def first_loss(nums):
    nums.sort()
    i, j = 0, 1
    while True:
        if i == len(nums):
            return j
        if nums[i] <= 0:
            i += 1
            continue
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        if nums[i] == j:
            i += 1
            j += 1
            continue
        return j

nums = [1, 2, 0]
nums_1 = [3, 4, -1, 1]
print(first_loss(nums_1))


























