# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/17 16:59
# @Author : San_mao_liu
# @File : Two_sum.py
# @Software: PyCharm


def two_sum(nums,target):
    """
    :param nums:
    :param target:
    :return:
    """
    for i in nums:
        j = target - i
        start_index = nums.index(i)
        next_index = start_index + 1
        temp_nums = nums[next_index:]
        if j in temp_nums:
            return (nums.index(i),next_index + temp_nums.index(j))


# nums = [2,7,11,15]
# target = 9
#
# d = two_sum(nums,target)
# print(d)


def two_Sum(nums,target):
    dict = {}
    for i in range(len(nums)):  # 遍历列表
        if target - nums[i] not in dict:
            dict[nums[i]] = i    # i是值，nums[i]是键
        else:
            return [dict[target - nums[i]],i]

        # print(dict)
# nums = [2,7,11,15]
# target = 9
