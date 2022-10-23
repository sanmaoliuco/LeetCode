# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 20:56
# @Author : San_mao_liu
# @File : youxiaokuohao.py
# @Software: PyCharm

def isValid(s):
    if len(s) % 2 == 1:
        return False

    pairs = {")":"(","]":"[","}":'{'}

    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:   # 判断栈是否为空，栈顶元素是否与正在遍历的匹配
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


s = "()[]{}"
# s = "({[}])"
# print(isValid(s))




def isvalid(s):

    dic = {'{':'}','(':')','[':']','?':'?'}

    stack = ['?']

    for ch in s:
        if ch in dic:       # 判断右括号是否在字典中，在则入栈
            stack.append(ch)

        elif dic[stack.pop()] != ch:    # ch如果为左括号，则栈中右括号作为key，在字典中查找对应的value
            return False

    return len(stack) == 1

# 不能pop一个空列表

def is_valid(s):
    dic = {'}':'{',')':'(',']':'['}
    stack = []

    for ch in s:
        if ch in dic.values():   # 右括号入账
            stack.append(ch)

        elif ch in dic.keys():    # ch如果是左括号
            if stack == [] or dic[ch] != stack.pop():
                return False
        else:
            return False
    return stack == []

print(is_valid(s))






# print(isvalid(s))





















