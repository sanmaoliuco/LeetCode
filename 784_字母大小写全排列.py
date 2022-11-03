# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/30 11:13
# @Author : San_mao_liu
# @File : 784_字母大小写全排列.py
# @Software: PyCharm


def letterCasePermutation(s):
    ans = []
    def dfs(idx, n, cur):
        if idx == n:
            ans.append(cur)
            return
        dfs(idx + 1, n, cur + s[idx])
        if 'a' <= s[idx] < 'z' or 'A' <= s[idx] <= 'Z':
            dfs(idx + 1, n, cur + s[idx].swapcase())

    dfs(0, len(s), '')
    return ans

s = "a1b2"

print(letterCasePermutation(s))

