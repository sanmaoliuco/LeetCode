# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/9 8:58
# @Author : San_mao_liu
# @File : 6.Z字形转换.py
# @Software: PyCharm


def Z_convert(s,numRow):
    if numRow == 0 or numRow > len(s):
        return s

    res = ['' for _ in range(numRow)]

    i,flag = 0 , -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRow - 1:
            flag = -flag

        i += flag

    return ''.join(res)


def convert(s,numRows):
    # cache 生成行数的列表例如以numRows = 3为例：
    """
    0       0
    1   1   1
    2
    然后整合成列表cache = [0,1,2,1]
    """
    cache = [i for i in range(numRows)] + [i for i in range(1,numRows - 1)][::-1]
    res = ['' for _ in range(numRows)]
    for i ,c in enumerate(s):
        res[cache[i%len(cache)]] += c

    return ''.join(res)


s = 'leetcod'
numRow = 3
print(Z_convert(s,numRow))



















