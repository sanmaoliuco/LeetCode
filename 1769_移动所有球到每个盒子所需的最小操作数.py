# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/2 10:31
# @Author : San_mao_liu
# @File : 1769_移动所有球到每个盒子所需的最小操作数.py
# @Software: PyCharm



def minOperations(boxes):
    res = []

    # 遍历小球的目的地
    for i in range(len(boxes)):
        s = 0
        # 操作数的遍历
        for j, c in enumerate(boxes):
            if c == '1':
                s += abs(i - j)
        res.append(s)

    return res

def min_operations(boxes):
    res = [0] * len(boxes)

    for i in range(len(boxes)):
        if boxes[i] == "0": continue
        for j in range(len(res)):
            res[j] += abs(i - j)

    return res

boxes = '110'
# print(minOperations(boxes))
print(min_operations(boxes))



