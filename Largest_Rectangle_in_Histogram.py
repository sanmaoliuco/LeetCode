# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/14 8:38
# @Author : San_mao_liu
# @File : Largest_Rectangle_in_Histogram.py
# @Software: PyCharm


"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""


def largestRectangleArea(heights):
    size = len(heights)
    res = 0

    for i in range(size):
        left = i
        cur_height = heights[i]
        while left > 0 and heights[left-1] >= cur_height:
            left -= 1

        right = i
        while right < size - 1 and heights[right+1] >= cur_height:
            right += 1

        max_width = right - left + 1

        res = max(res,cur_height * max_width)

    return res

heights = [2,1,5,6,2,3]
print(len(heights))
n = largestRectangleArea(heights)
print(n)


























