# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/29 9:58
# @Author : San_mao_liu
# @File : 1758_生成交替二进制字符串的最少操作数.py
# @Software: PyCharm


def minOperation(s):
    cnt = sum(int(c) != i % 2 for i, c in enumerate(s))
    return min(cnt, len(s) - cnt)

s = '0100'
c = 'abcderf'


# print(minOperation(s))

def min_operation(s):
    # 以1开头的字符串
    a = s[0::2].count('1') + s[1::2].count('0')
    # 以0 开头的字符串
    b = s[0::2].count('0') + s[1::2].count('1')
    return min(a, b)

# print(min_operation(s))

print(s[1::2].count('0'))










