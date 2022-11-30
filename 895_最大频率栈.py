# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/30 9:38
# @Author : San_mao_liu
# @File : 895_最大频率栈.py
# @Software: PyCharm
from collections import defaultdict


class FreqStack:
    def __init__(self):
        # 每个元素出现的频率
        self.freq_stack = defaultdict(int)
        # key为频率，value为元素
        self.stack = defaultdict(list)
        # 记录最大频率
        self.max_freq = 0

    def push(self, val):
        self.freq_stack[val] += 1
        self.stack[self.freq_stack[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq_stack[val])


    def pop(self):
        # 最大频率的value，pop
        val = self.stack[self.max_freq].pop()
        # pop出一个value，其对应频率减一
        self.freq_stack[val] -= 1
        # 判断频率最大的栈中是否还有元素，没有就将其减一
        if len(self.stack[self.max_freq]) == 0:
            self.max_freq -= 1

        return val













