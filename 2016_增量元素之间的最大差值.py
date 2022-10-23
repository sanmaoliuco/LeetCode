# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/7 8:59
# @Author : San_mao_liu
# @File : 2016_增量元素之间的最大差值.py
# @Software: PyCharm


def maximumDfference(nums):

    n = len(nums)
    max1 = 0
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] >nums[i]:
                max1 = max(max1,nums[j] - nums[i])
            # elif max1 == 0:
            #     return -1

    return max1 if max1!= 0 else -1

nums1 = [9,4,3,2]
nums2 = [1,5,2,10]
nums3 = [7,1,5,4]

print(maximumDfference(nums1))
print(maximumDfference(nums2))
print(maximumDfference(nums3))


















