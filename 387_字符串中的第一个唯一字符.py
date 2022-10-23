# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/8 8:31
# @Author : San_mao_liu
# @File : 387_字符串中的第一个唯一字符.py
# @Software: PyCharm

import collections
def firstUniqChar(s):

    frequency = collections.Counter(s)
    print(frequency)

    for i, ch in enumerate(s):
        if frequency[ch] == 1:
            return i

    return -1


def first_uniq_char(s):
    dic = {}

    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for index,val in enumerate(s):
        if dic[val] == 1:
            return index

    return -1


def first_uni_ch(s):
    dic = {}
    q = []

    for i,ch in enumerate(s):
        if ch not in dic:
            dic[ch] = i
            q.append((s[i],i))
        else:
            dic[ch] = -1
            while q and dic[q[0][0]] == -1:
                q.pop()

    return -1 if not q else q[0][1]

def fir_un_char(s):
    d = {}
    for index, val in enumerate(s):
        if val not in d:
            d[val] = index
        else:
            del d[val]

    return min(d.values()) if d else -1

s = 'leetcode'
# print(firstUniqChar(s))
# print(first_uniq_char(s))
# print(first_uni_ch(s))
print(fir_un_char(s))






