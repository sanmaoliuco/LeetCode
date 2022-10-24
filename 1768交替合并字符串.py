# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/23 11:03
# @Author : San_mao_liu
# @File : 1768交替合并字符串.py
# @Software: PyCharm

# 暴力求解
def mergeAlternately(word1,word2):
    n = len(word1)
    m = len(word2)

    s = ''
    if n > m:
        for i in range(m):
            s += word1[i] + word2[i]

        s += word1[m:]
        return s
    else:
        for j in range(n):
            s += word1[j] + word2[j]

        s += word2[n:]
        return s


#双指针
def mer_word(word1, word2):
    m,n = len(word1),len(word2)

    i, j = 0, 0
    ans = []
    while i < m or j < n:
        if i < m:
            ans.append(word1[i])
            i += 1
        if j < n:
            ans.append(word2[j])
            j += 1

    return "".join(ans)




word1 = "ab"
word2 = "pqrs"

print(mer_word(word1,word2))






