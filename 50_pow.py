# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/17 9:47
# @Author : San_mao_liu
# @File : 50_pow.py
# @Software: PyCharm

def myPow(x, n):

    def quickM(x, n):
        if n == 0:
            return 1.0

        y = quickM(x, n // 2)
        return y * y if n % 2 == 0 else y * y * x
    return quickM(x, n) if n >= 0 else 1 / quickM(x, -n)

x = 2
n = 10

print(myPow(x, n))


# a = 'bac'
# b = 'abc'
# # list(a).sort()
# print(sorted(a))
# print(list(b))
