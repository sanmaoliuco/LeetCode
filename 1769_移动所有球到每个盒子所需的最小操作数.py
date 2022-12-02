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

def min_Operations(boxes):
    n = len(boxes)
    left, right = [0] * n, [0] * n
    cur = 0
    for i, c in enumerate(boxes):
        left[i], cur = left[i - 1] + cur, cur + (c == '1')
    cur = int(boxes[-1] == '1')
    for i in range(n - 2, -1, -1):
        right[i], cur = right[i + 1] + cur, cur + (boxes[i] == '1')

    return [left[i] + right[i] for i in range(n)]


boxes = '110'
# print(minOperations(boxes))
# print(min_operations(boxes))
print(min_Operations(boxes))



