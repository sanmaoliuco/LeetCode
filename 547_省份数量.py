# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/5/7 15:49
# @Author : San_mao_liu
# @File : 547_省份数量.py
# @Software: PyCharm


def find_circle_num(isConnected):
    if not isConnected:return 0
    n = len(isConnected)

#     创建并查集
    p = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1:
                _union(p, i, j)

    return len(set([_parent(p, i) for i in range(n)]))


def _union(p, i, j):
    p1 = _parent(p, i)
    p2 = _parent(p, j)
    p[p2] = p1

def _parent(p, i):
    root = i
    while p[root] != root:
        root = p[root]
    while p[i] != i:
        x = i; i = p[i]; p[x] = root

    return root






