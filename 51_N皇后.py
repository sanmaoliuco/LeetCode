# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/18 10:21
# @Author : San_mao_liu
# @File : 51_N皇后.py
# @Software: PyCharm


def solveNQueens(n):
    res = []

    def dfs(cols, xy_dif, xy_sum):
        # terminator
        row = len(cols)
        if row == n:
            res.append(cols)

        for col in range(n):
            if col not in cols and row - col not in xy_dif\
                and row + col not in xy_sum:

                dfs(cols + [col], xy_dif + [row - col], xy_sum + [row + col])

    dfs([],[],[])



    return [['.' * i + 'Q' + '.' * (n - i -1) for i in col] for col in res]


n = 4

print(solveNQueens(n))




























