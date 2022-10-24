# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/23 11:17
# @Author : San_mao_liu
# @File : 10正则匹配.py
# @Software: PyCharm

#递归
def isMatch(s,p):

    if len(p) == 0:
        return len(s) == 0

    first_match = len(s) >= 1 and (s[0] == p[0] or p[0] == '.')
    if len(p) >= 2 and p[1] == "*":
        return isMatch(s,p[2:]) or (first_match and isMatch(s[1:], p))

    return first_match and isMatch(s[1:], p[1:])

# 记忆化搜索
from functools import lru_cache
def is_match(s, p):

    @lru_cache(None)
    def DFS(i, j):
        if j == len(p):
            return i == len(s)
        first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if j + 1 < len(p) and p[j+1] == "*":
            return DFS(i, j + 2) or (first_match and DFS(i + 1, j))
        return first_match and DFS(i + 1, j + 1)
    return DFS(0, 0)

s = 'abx'
p = ".*"
print(is_match(s,p))













