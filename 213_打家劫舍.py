# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/20 8:38
# @Author : San_mao_liu
# @File : 213_打家劫舍.py
# @Software: PyCharm

def rob(nums):
    if nums == None or len(nums) == 0:
        return 0

    a = [[0, 0] for _ in range(len(nums))]
    a[0][0] = 0
    a[0][1] = nums[0]

    for i in range(len(nums)):
        a[i][0] = max(a[i - 1][0], a[i - 1][1])
        a[i][1] = a[i - 1][0] + nums[i]

    return max(a[len(nums) - 1][0], a[len(nums) - 1][1])

# 二维dp
def rob_1(nums):
    if nums == None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    a = [[0, 0] for _ in range(len(nums))]
    res1 = res2 = 0
    # 偷第一间房，不偷最后一间房，下标范围[0, n-2]
    for i in range(0, len(nums) - 1):
        a[0][0] = 0
        a[0][1] = nums[0]
        a[i][0] = max(a[i - 1][0], a[i - 1][1])
        a[i][1] = a[i-1][0] + nums[i]
        res1 = max(a[len(nums) - 2][0], a[len(nums) - 2][1])
    # 不偷第一间房，偷最后一间房，下标范围[1, n - 1]
    for i in range(1, len(nums)):
        a[1][0] = 0
        a[1][1] = nums[1]
        a[i][0] = max(a[i-1][0], a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]
        res2 = max(a[len(nums) - 1][0], a[len(nums) - 1][1])

    return max(res1, res2)


# 一维dp
def rob_2(nums):
    def my_rob(nums):
        pre = cur = 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur
    return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

def rob_3(nums):
    def my_rob1(nums):
        now = pre = 0
        for n in nums:
            now, pre = max(pre + n, now), now
        return now
    return max(my_rob1(nums[len(nums) != 1 : ]), my_rob1(nums[:-1]))



nums = [1,2,3]
# print(nums[len(nums) != 1:])
# print(len(nums) != 1)
# print(rob_2(nums))
print(rob_3(nums))



















