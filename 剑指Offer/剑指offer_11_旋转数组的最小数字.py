# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/3 20:09
# @Author : San_mao_liu
# @File : 剑指offer_11_旋转数组的最小数字.py
# @Software: PyCharm

def minArray(numbers):
    dic = {}
    for key, val in enumerate(numbers):
        dic[val] = key

    numbers.sort()
    print(numbers)
    print(dic)

    return dic[numbers[0]]

numbers = [2,2,2,0,1]
print(minArray(numbers))