# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/5 9:18
# @Author : San_mao_liu
# @File : 杨辉三角.py
# @Software: PyCharm

def generate(numRows):

    if numRows == 0:
        return []
    res = [[1]]

    for i in range(numRows-1):
        temp = [a+b for a,b in zip([0] + res[-1],res[-1] + [0])]
        # res是一个二维数组，res[-1]是一个列表，[0]+res[-1]就是相当于往res中的最后一个列表中
        # 在头部添加元素，zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个
        # 元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长
        # 度与最短的对象相同，利用*号操作符，可以将元组解压为列表
        res.append(temp)
    return res

print(generate(5))














