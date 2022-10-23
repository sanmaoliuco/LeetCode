# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/3 17:58
# @Author : San_mao_liu
# @File : 389_找不同.py
# @Software: PyCharm

import collections
def findTheDifference(s, t):
    pass

s = 'abc'
d = 'abcd'

A = collections.Counter(s)
B = collections.Counter(d)
print(A)
print(list(B-A)[0])


print(ord('e'))
sum_1 = 0
sum_1 += sum([ord(i) for i in s])

print(sum_1)




