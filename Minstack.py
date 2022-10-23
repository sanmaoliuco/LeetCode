# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/13 8:43
# @Author : San_mao_liu
# @File : Minstack.py
# @Software: PyCharm

"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。



"""

"""
思路分析：
    1、辅助栈与数据栈同步
    2、辅助栈与数据栈不同步
"""
# 1、同步
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.data.append(val)
        if len(self.helper)==0 or val <= self.helper[-1]:
            self.helper.append(val)
        else:
            self.helper.append(self.helper[-1])


    def pop(self):
        """
        :rtype: None
        """

        if self.data:
            self.helper.pop()
            return self.data.pop()



    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]


# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

s = MinStack()

t = ["MinStack","push","push","push","getMin","pop","top","getMin"]
p = [[],[-2],[0],[-3],[],[],[],[]]

for i in p:
    for j in i:
        s.push(j)

for i in range(len(p)):
    print(s.getMin(),s.pop())
    



