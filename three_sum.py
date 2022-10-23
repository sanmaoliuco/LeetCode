# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/5 20:42
# @Author : San_mao_liu
# @File : three_sum.py
# @Software: PyCharm


def threeSum(nums):

    nums.sort()      # 先对数组进行排序
    res = []      # 初始化一个空列表
    if not nums or len(nums) < 3:     # 判断数组是否为空或者个数是否小于三
        return []

    for i in range(len(nums)):     # i即为目标值，从排序后的数组从头开始遍历
        if nums[i] > 0:     # 如果num[i]值大于零则返回res
            return res
        if i>0 and nums[i] == nums[i-1]:   # 如果当前遍历的num[i]等于之前遍历过得num[i-1]  则对当前值不再进行计算，避免重复
            continue

        L = i+1         # 初始化双指针
        R = len(nums) - 1

        while L < R:    # 右指针要大于左指针
            if nums[i] + nums[L] + nums[R] == 0:   # 满足条件append到res列表中
                res.append([nums[i],nums[L],nums[R]])

                while L < R and nums[L] == nums[L+1]:   #  左指针右移，右指针左移
                    L += 1
                while L < R and nums[R] == nums[R - 1]:
                    R -= 1

                L += 1    # update左右指针
                R -= 1

            elif nums[i] + nums[L] + nums[R] > 0 :    # nums[R] 比较大 右指针左移
                R -= 1
            else:         # nums[L] 比较小  左指针右移
                L += 1

    return res


nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

print(nums[:-2])


def three_sum(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    res = set()

    for i,v in enumerate(nums[:-2]):
        if i>= 1 and v == nums[i-1]:
            continue

        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 2

            else:
                res.add((v,-v-x,x))

    return map(list,res)

print(three_sum(nums))














