# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/26 10:39
# @Author : San_mao_liu
# @File : 862_和至少为k的最短子数组.py
# @Software: PyCharm

from collections import deque

def shortests_subarray(nums, k):
    preSumArr = [0]
    res = len(nums) + 1
    # 前缀和
    for num in nums:
        preSumArr.append(preSumArr[-1] + num)
    # print(preSumArr)
    # 设置一个双端队列
    q = deque()
    # 遍历前缀和
    for i,curSum in enumerate(preSumArr):
        while q and curSum - preSumArr[q[0]] >= k:
            # 找到符合条件的最短子数组
            res = min(res, i - q.popleft())
        while q and preSumArr[q[-1]] >= curSum:
            q.pop()
        q.append(i)
    return res if res < len(nums) + 1 else -1

nums = [2, -1, 2]
print(shortests_subarray(nums,k=3))















