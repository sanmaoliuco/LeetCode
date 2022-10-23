# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/4 17:02
# @Author : San_mao_liu
# @File : 496_下一个更大的元素.py
# @Software: PyCharm


def nextGreaterElement(nums1,nums2):

    res = {}
    stack = []

    for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:

            res[stack.pop()] = nums2[i]

        stack.append(nums2[i])

    while stack:
        res[stack.pop()] = -1

    print(res)
    print([res[num] for num in nums1])



nums1 = [4,1,2]
nums2 = [1,3,4,2]

nextGreaterElement(nums1,nums2)


def next_greater_element(nums1, nums2):

    res = {}
    stack = []

    for num in reversed(nums2):
        while stack and num < stack[-1]:
            res[num] = stack.pop()

        stack.append(num)

    while stack:
        res[stack.pop()] = -1

    print(res)

next_greater_element(nums1, nums2)











