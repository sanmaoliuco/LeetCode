# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/1 20:20
# @Author : San_mao_liu
# @File : 8_字符串转换整数.py
# @Software: PyCharm


def myAtoi(s):
    ls = list(s.strip())

    if len(ls) == 0 :
        return  0

    # print(ls)

    sign = -1 if ls[0] == '-' else 1

    if ls[0] in ['-','+'] : del ls[0]
    ret , i = 0 , 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + ord(ls[i]) - ord('0')   # ASCII 下转换为整数
        i += 1

    return max(-2**31,min(sign * ret,2**31-1))


s = '     -42'
print(myAtoi(s))

ls = list(s.strip())
print(ls)
# print(ord(ls[1]))
# print(ord('0'))

l = ord('5') - ord('0')
print(l)

















