# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/22 20:22
# @Author : San_mao_liu
# @File : 198_打家劫舍.py
# @Software: PyCharm

def rob(nums):
    if nums == None or len(nums) == 0:
        return 0

    a = [[0,0] for _ in range(len(nums))]
    print(a)
    a[0][0] = 0
    a[0][1] = nums[0]

    for i in range(len(nums)):
        a[i][0] = max(a[i-1][0],a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]

    return max(a[len(nums) - 1][0],a[len(nums) - 1][1])

nums = [1,2,3,4]
# print(rob(nums))


def rob_2(nums):
    if nums == None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    a = [[0,0] for _ in range(len(nums))]
    # res1 = 0
    # res2 = 0
    # a[0][0] = 0
    # a[0][1] = nums[0]
    for i in range(0,len(nums)-1):
        a[0][0] = 0
        a[0][1] = nums[0]
        a[i][0] = max(a[i-1][0],a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]
        res1 = max(a[len(nums)-2][0],a[len(nums)-2][1])

    for i in range(1,len(nums)):
        a[1][0] = 0
        a[1][1] = nums[1]
        a[i][0] = max(a[i - 1][0], a[i - 1][1])
        a[i][1] = a[i - 1][0] + nums[i]
        res2 = max(a[len(nums)-1][0],a[len(nums)-1][1])

    return max(res1,res2)
nums1 = [2,3,2]
print(rob_2(nums))
print(rob_2(nums1))

import math
c = int(math.sqrt(5))
print(c)




a = [[0, 0]] * 4
b = [[0, 0] for _ in range(len(nums))]

print(a)
print(b)










