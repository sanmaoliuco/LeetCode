# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/29 10:23
# @Author : San_mao_liu
# @File : 剑指offer_09_用两个栈实现队列.py
# @Software: PyCharm

'''
栈：先入后出
队列：先入先出
两个栈实现队列，一个栈入队，一个栈出队
第一个栈入，第二个栈实现第一个栈的倒序（先入后出实现队列元素的删除）

'''


class CQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []


    def appendTail(self, value):
        self.in_stack.append(value)


    def deleteHead(self):
        # 判断出栈的栈中是否有元素，有就出栈，实现队列中的出队
        if self.out_stack:return self.out_stack.pop()
        # 判断入栈的栈中是否有元素，为空返回-1
        if not self.in_stack:return -1
        # 否则将入栈的栈中元素出栈加入到出栈的栈中
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()


cQ = CQueue()
print(cQ.appendTail(3))
print(cQ.deleteHead())
print(cQ.deleteHead())











