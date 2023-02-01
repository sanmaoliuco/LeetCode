# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/2 16:17
# @Author : San_mao_liu
# @File : 2485_找出中枢整数.py
# @Software: PyCharm

def pivotInteger(n):
    m = (n * (n + 1)) / 2
    x = int(m ** 0.5)
    return x if x * x == m else -1

def pivot_integer(n):
    for x in range(1, n + 1):
        s1 = 0
        for y in range(1,x + 1):
            s1 += y

        s2 = 0
        for y in range(x, n + 1):
            s2 += y
        if s1 == s2:
            return x
    return -1


n = 8
print(pivotInteger(n))
print(pivot_integer(8))

