# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/17 15:08
# @Author : San_mao_liu
# @File : 17_电话号码的字母组合.py
# @Software: PyCharm

def letterCombinations(digits):
    if not digits:
        return []

    dic = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
    }
    res = []

    def search(s, digits, i, res, dic):
        if i == len(digits):
            res.append(s)
            return

        letters = dic[digits[i]]    # 读出输入数所对应的字母
        for j in range(len(letters)):
            search(s + letters[j], digits, i + 1, res, dic)

    search("", digits, 0, res, dic)

    return res


def letter_combinations(digits):
    if not digits:
        return list()

    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(index):
        # terminator
        if index == len(digits):
            res.append("".join(tmp))

        else:
            digit = digits[index]
            for letter in dic[digit]:
                tmp.append(letter)
                backtrack(index + 1)  # 递归
                tmp.pop()  # 回溯

    res = []
    tmp = []

    backtrack(0)

    return  res

def letter_Combination(digits):
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(dic[digits[0]])

    prev = letterCombinations(digits[:-1])
    additional = dic[digits[-1]]

    return [s + c for s in prev for c in additional]

def letter_Combinations(digits):
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    cmp = [''] if digits else []
    for d in digits:
        cmp = [p + q for p in cmp for q in dic[d]]

    return cmp



digits = "234"
# print(letter_Combination(digits))
print(letter_combinations(digits))
# print(digits[:-1])
# print(letterCombinations(digits))
#
# print(letter_combinations(digits))






