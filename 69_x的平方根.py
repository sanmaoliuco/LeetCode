# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/24 8:24
# @Author : San_mao_liu
# @File : 69_x的平方根.py
# @Software: PyCharm

def my_sqrt(x):
    if x == 0 or x == 1:
        return x

    left = 1
    right = x
    while left < right:
        mid = left + (right - left)// 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    #     if mid * mid > x:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return mid

'''
    def mySqrt(self, x: int) -> int:
        left , right = 1, x 
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x :
                left = mid + 1
            else:
                right = mid - 1
                

        return right
'''

def my_s(x):
    if x <= 0:
        return
    cur = 1
    while True:
        pre = cur
        cur = (cur + x/cur) / 2
        if abs(cur - pre) < 1e-6:
            return int(cur)

def my_sq(x):
    r = x
    while r * r > x:
        r = (r + x/r)/2
    return int(r)


x = 4
print(my_sqrt(x))
print(my_s(x))
print(my_sq(x))
















