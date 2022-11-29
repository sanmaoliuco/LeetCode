# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/29 10:54
# @Author : San_mao_liu
# @File : 剑指offer_30_包含min函数的栈.py
# @Software: PyCharm

# import math
#
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         # 辅助栈
#         self.min_stack = [math.inf]
#
#     def push(self,x):
#         self.stack.append(x)
#         # 始终放最下的元素
#         self.min_stack.append(min(x, self.min_stack[-1]))
#         return self.stack, self.min_stack
#
#     def pop(self):
#         self.stack.pop()
#         self.min_stack.pop()
#         return self.stack, self.min_stack
#     def top(self):
#         return self.stack[-1]
#
#
#     def min(self):
#         return self.min_stack[-1]


class Min_Stack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack, self.min_stack = [], []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

        return self.stack, self.min_stack

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack, self.min_stack

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]
Min_stack = Min_Stack()
print(Min_stack.push(-2))
print(Min_stack.push(0))
print(Min_stack.push(-1))
print(Min_stack.min())
print(Min_stack.pop())
print(Min_stack.top())
print(Min_stack.min())













