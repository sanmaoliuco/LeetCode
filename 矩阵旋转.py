# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/29 19:51
# @Author : San_mao_liu
# @File : 矩阵旋转.py
# @Software: PyCharm



def rotateMatrix(mat, n):

    if n % 2 == 0:
        mid1 = n / 2
        mid2 = n / 2
    else:
        mid1 = n / 2 + 1
        mid2 = n / 2
    for i in range(mid1):
        for j in range(mid2):
            tmp = mat[j][n-1-i]
            mat[j][n-1-i] = mat[i][j]
            tmp2 = mat[n-1-i][n-1-j]
            mat[n-1-i][n-1-j] = tmp
            tmp = mat[n-1-j][i]
            mat[n-1-j][i] = tmp2
            mat[i][j] = tmp

    return mat


def slice_num(s):
    if int(s) % 2 == 0:
        return -1
    l1 = []
    for i in range(len(s)):
        a = []
        b = []
        if int(s[i]) % 2 != 0:
            a.append(s[:i+1])
        l1.append(a)
    return l1



s = '32323'
print(slice_num(s))

