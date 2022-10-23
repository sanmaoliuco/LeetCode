# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/4 20:33
# @Author : San_mao_liu
# @File : 并查集.py
# @Software: PyCharm

"""
makeSet(s): 建立一个新的并查集，其中包含s个元素集合
unionSet(x,y):把元素x和元素y所在的集合合并，要求x和y所在的集合不想交，
如果相交则不合并

find(x):找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个
集合，只要将它们各自的代表比较一一下就可以了

"""

'''
并查集Python代码实现


def init(p):
    p = [i for i in range(n)]

def union(self,p,i,j):
    p1 = self.parent(p,i)
    p2 = self.parent(p,j)
    p[p1] = p2

def parent(self,p,i):
    root = i
    while p[root] != root:
        root = p[root]
    while p[i] != i:  # 路径压缩
        x = i
        i = p[i]
        p[x] = root

    return root

'''
result = []
def generateParenthesis(n):
    _generate(0, 0, n, "")
    return result

def _generate(left, right, n, s):
    if left == n and right == n:
        result.append(s)
        return

    if left < n:
        _generate(left + 1, right, n, s + "(")
    if right < left:
        _generate(left, right + 1, n, s + ")")


print(generateParenthesis(1))










