# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/6 19:45
# @Author : San_mao_liu
# @File : binary_search.py
# @Software: PyCharm

"""
二分查找的前提
    1、目标函数单调性（单调递增或者递减）
    2、存在上下界（bounded）
    3、能够通过索引访问（index accessible）

"""

# 代码模板
"""
left,right = 0,len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
"""
# 二分查找
def mySqrt(x):
    left , right = 1,x
    while left <= right:
        mid = left + (right - left) // 2
        if mid*mid == x:
            return mid
        elif mid*mid > x :
            right = mid - 1
        else:
            left = mid + 1
    return right

# 牛顿迭代法
def my_sqrt(x):
    if x == 0 :
        return 0
    x0 , c = float(x),float(x)

    while True:
        xi = (x0 + c/x0) / 2
        if abs(xi - x0) < 1e-7:
            break
        x0 = xi
    return int(x0)

print(mySqrt(12))

print(my_sqrt(12))


















