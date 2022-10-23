# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/15 21:25
# @Author : San_mao_liu
# @File : Anagram.py
# @Software: PyCharm

import string
import collections
def isAnagram(s,t):
    for c in string.ascii_lowercase:
        print(type(s.count(c)))
        return s.count(c) == t.count(c)


# s = "anagram"
# t = "anmarag"

def is_Anagram(s,t):
    if len(s) != len(t):
        return False

    count = collections.defaultdict(int)
    print(count)
    print(type(count))


    for c in s:
        count[c] += 1
        print(count)

    for c in t:
        count[c] -= 1

        if count[c] < 0:
            return False
    return True

# print(is_Anagram(s,t))



def latter(s,t):

    a = list(s)
    b = list(t)

    print(a.sort(),b.sort())

    if a.sort() == b.sort():
        print('1')

        return True

s = 'car'
b = 'rat'

latter(s,b)

















