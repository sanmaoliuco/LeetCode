# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/18 8:51
# @Author : San_mao_liu
# @File : 131_分割回文串.py
# @Software: PyCharm


def partition(s):

    res = []
    temp = []

    def backtrack(s,start_index):
        if start_index >= len(s):
            return res.append(temp[:])

        for i in range(start_index,len(s)):
            p = s[start_index:i+1]

            if p == p[::-1]:
                temp.append(p)
            else:continue
            backtrack(s,i+1)
            temp.pop()

    backtrack(s,0)
    return res


s = "aab"
print(partition(s))

print(s)
print(s[:])












