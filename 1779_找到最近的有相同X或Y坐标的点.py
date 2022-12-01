# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/1 9:37
# @Author : San_mao_liu
# @File : 1779_找到最近的有相同X或Y坐标的点.py
# @Software: PyCharm

import math

def nearestValidPoint(x, y, points):

    dic = {}
    dis_min = math.inf
    # di = []
    for point in points:
        if x == point[0] or y == point[1]:
            dis_min = min(dis_min, (abs(x - point[0]) + abs(y - point[1])))
            # di.append(dis_min)
            if dis_min in dic:
                dic[dis_min].append(points.index(point))
                # print(dic)
            else:
                dic[dis_min] = [points.index(point)]

    # print(dic.keys())

            # dic[dis_min].append(points.index(point))

    if dic:
        return dic[min(dic.keys())][0]
    else:
        return -1

def nearest_valid_point(x, y, points):
    ans, mi = -1, math.inf

    for i, (a, b) in enumerate(points):
        if a == x or b == y:
            d = abs(a - x) + abs(b - y)
            if d < mi:
                ans, mi = i, d

    return ans



x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# print(nearestValidPoint(x, y, points))
print(nearest_valid_point(x, y, points))










