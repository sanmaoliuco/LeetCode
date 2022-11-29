# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/29 15:20
# @Author : San_mao_liu
# @File : 剑指offer_04_二维数组中的查找.py
# @Software: PyCharm

def findNumberIn2DArray(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if target == matrix[i][j]:
                return True

    return False


# 二分查找
import bisect
# 内置二分查找，列表有序，返回值为索引
# bisect() 和 bisect_right()等同
def find_number_in2d_array(matrix, target):
    for row in matrix:
        idx = bisect.bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
    return False

"""
如果列表中没有元素x，那么bisect_left(ls, x)和bisect_right(ls, x)返回相同的值，该值是x在ls中“合适的插入点索引，使得数组有序”。此时，ls[index2] > x，ls[index3] > x。
"""
ls = [1, 5, 9, 13, 17]
index1 = bisect.bisect(ls, 7)
index2 = bisect.bisect_left(ls, 7)
index3 = bisect.bisect_right(ls, 7)
print('index1 = {}, index2 = {}, index3 = {}'.format(index1, index2,index3))

'''
如果列表中只有一个元素等于x，那么bisect_left(ls, x)的值是x在ls中的索引，ls[index2] = x。而bisec_right(ls, x)的值是x在ls中的索引加1，ls[index3] > x。
'''
ls = [1, 5, 9, 13, 17]
index1 = bisect.bisect(ls, 9)
index2 = bisect.bisect_left(ls, 9)
index3 = bisect.bisect_right(ls, 9)
print('index1 = {}, index2 = {}, index3 = {}'.format(index1, index2,index3))

"""
如果列表中存在多个元素等于x，那么bisect_left(ls, x)返回最左边的那个索引，此时ls[index2] = x。bisect_right(ls, x)返回最右边的那个索引加1，此时ls[index3] > x。
"""
ls = [1, 5, 5, 5, 17]
idx1 = bisect.bisect(ls, 5)
idx2 = bisect.bisect_left(ls, 5)
idx3 = bisect.bisect_right(ls, 5)
print('idx1 = {}, idx2 = {}, idx3 = {}'.format(idx1, idx2, idx3))





# 转化为“二叉搜索树” 图，从左下角开始往上递推

def find_Number_in2d_array(matrix, target):
    i, j = len(matrix) - 1, 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
        else:
            return True

    return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

# print(findNumberIn2DArray(matrix, 5))
# print(find_number_in2d_array(matrix, 5))



