# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/24 9:13
# @Author : San_mao_liu
# @File : 367_有效的完全平方数.py
# @Software: PyCharm

def is_pre(num):
    x = 1
    square = 1
    while square <= num:
        if square == num:
            return True
        x += 1
        square = x * x
    return False

def is_pref(num):
    left, right = 0, num//2
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid +1
        else: right = mid - 1
    return False

print(is_pref(1))

#
# print(is_pre(14))
