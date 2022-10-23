# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/31 9:28
# @Author : San_mao_liu
# @File : Generate_Parentheses.py
# @Software: PyCharm

'''
22 括号的生成

'''

def generateParenthesis(n):
    ans = []
    def backtrack(S,left,right):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S,left + 1,right)
            S.pop()

        if right < left:
            S.append(")")
            backtrack(S,left,right + 1)
            S.pop()

    backtrack([],0,0)
    return ans

k = generateParenthesis(3)
print(k)

















