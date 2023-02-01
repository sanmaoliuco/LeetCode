# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/3 19:34
# @Author : San_mao_liu
# @File : 1796_字符串中第二大的数字.py
# @Software: PyCharm


def secondHighest(s):
    d = list(''.join(filter(str.isdigit,s)))
    l1 = []
    for i in range(len(d)):
        if d[i] in l1:
            continue
        l1.append(d[i])
    l1.sort()
    l1.reverse()
    print(l1)
    return l1[1] if len(l1) != 1 else -1

s = "ck077"
print(secondHighest(s))

def second_Highest(s: str) -> int:
    first = second = -1
    for c in s:
        if c.isdigit():
            num = int(c)
            if num > first:
                second = first
                first = num
            elif second < num < first:
                second = num
    return second

print(second_Highest(s))


