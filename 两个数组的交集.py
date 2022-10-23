# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/28 9:31
# @Author : San_mao_liu
# @File : 两个数组的交集.py
# @Software: PyCharm

import collections
def intersect(nums1, nums2):

    dic1 = collections.Counter(nums1)
    dic2 = collections.Counter(nums2)

    num = dic1 & dic2

    return list(num.elements())

nums1 = [1,2,2,2,1,3]
nums2 = [3,2,2,2,3]
dic1 = collections.Counter(nums1)
dic2 = collections.Counter(nums2)
print(dic1)
print(dic2)
print(dic1 & dic2)
print(intersect(nums1,nums2))
