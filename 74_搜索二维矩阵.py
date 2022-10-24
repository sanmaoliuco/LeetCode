# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/24 9:25
# @Author : San_mao_liu
# @File : 74_搜索二维矩阵.py
# @Software: PyCharm

def search_matrix(matrix, target):
    if len(matrix) == 0:
        return False
    row, col = 0, 0
    while row < len(matrix) and col < len(matrix[0]):
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col += 1
        else: return True

    return False

matrix = [
    [1,2,3,4],
    [5,6,7,8]
]
target = 5

print(search_matrix(matrix,target))







