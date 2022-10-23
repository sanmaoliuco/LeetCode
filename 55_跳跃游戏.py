# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/11 8:28
# @Author : San_mao_liu
# @File : 55_跳跃游戏.py
# @Software: PyCharm


def canJump(nums):
    max_distance = 0   # 初始化最大距离
    for i, jump in enumerate(nums):  # 枚举

        #最大距离大于当前下标并且当前下标加跳跃距离大于目前的最大距离就更新最大距离
        if max_distance >= i and i + jump > max_distance:
            max_distance = i + jump
    # 遍历结束如果最大距离大于数组长度减一则返回true，否则返回false
    return max_distance >= len(nums) - 1

def can_Jump(nums):
    max_distance = 0
    for i in range(len(nums)):
        if max_distance >= i:
            max_distance = max(max_distance, nums[i] + i)

            if max_distance >= len(nums) - 1:
                return True
    return False


def can_jump(nums):
    dp = [0] * len(nums)
    for i in range(0,len(nums)):
        if dp[i - 1] >= i:
            dp[i] = max(dp[i - 1], i + nums[i] )
            if dp[i-1] >= len(nums) - 1:
                return True
    return False


# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
# print(canJump(nums))
# print(can_Jump(nums))
print(can_jump(nums))






















