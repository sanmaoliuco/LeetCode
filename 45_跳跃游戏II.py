# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/12 9:47
# @Author : San_mao_liu
# @File : 45_跳跃游戏II.py
# @Software: PyCharm


def jump(nums):
    res = [i for i in range(len(nums))]
    for i in range(len(nums)):
        temp = i + nums[i]

        for j in range(i,temp+1):
            if j < len(nums):
                res[j] = min(res[j],res[i] + 1)

    return res[-1]

def Jump(nums):
    n = len(nums)

    if n <= 1:
        return 0

    step = [i for i in range(n)]

    for i in range(n-1):
        # if step[i] < n + 1:
            l = nums[i] + i
            for j in range(1, l):
                if (j + i) < len(nums):
                    step[j + i] = min(step[i] + 1, step[j + i])

    return step[n - 1]
nums = [2,3,0,1,4]
print(Jump(nums))
