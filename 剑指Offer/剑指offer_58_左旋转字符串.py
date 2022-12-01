
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/1 10:45
# @Author : San_mao_liu
# @File : 剑指offer_58_左旋转字符串.py
# @Software: PyCharm

def reverseLeftWords(s, n):
    return s[n:] + s[:n]


def reverse_left_words(s, n):
    res = []
    for i in range(n, len(s)):
        res.append(s[i])

    for j in range(0, n):
        res.append(s[j])

    return "".join(res)

s = "abcdefg"
k = 2
print(reverseLeftWords(s, 2))
print(reverse_left_words(s, 2))