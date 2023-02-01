# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/3 20:18
# @Author : San_mao_liu
# @File : 剑指offer_50_第一个只出现一次的字符.py
# @Software: PyCharm

def firstUniqChar(s):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for items in dic:
        if dic[items] == 1:
            return items

s = "loveleetcode"

# print(firstUniqChar(s))
def isCir(sentence):
    if len(sentence) == 1:
        if sentence[0] == sentence[-1]:
            return True
        else:
            return False

    words = sentence.split()
    if words[0][0] == words[-1][-1]:
        for i in range(len(words) - 1):
            if words[i][-1] == words[i + 1][0]:
                continue
            else:
                return False

        return True
    return False


# sentence = 'Leetcode is cool'
# print(isCir(sentence))


def dividePlayer(skill):
    skill.sort()
    i, j = 1, len(skill) - 2
    target = skill[0] + skill[-1]
    l1 = []
    while i < len(skill) and j > 0:
        s = []
        if skill[i] + skill[j] == target :
            s.append(skill[i])
            s.append(skill[j])
            l1.append(s)
        else: return -1
        i += 1
        if i == j: break
        j -= 1

    sum = 0
    l1.append([skill[0], skill[-1]])

    for num in l1:
        sum += num[0] * num[1]

    return sum


skill = [3,2,5,1,3,4]
print(dividePlayer(skill))







