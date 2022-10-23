# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/9 9:27
# @Author : San_mao_liu
# @File : 692_前k个高频单词.py
# @Software: PyCharm

from collections import defaultdict
import collections

def topKFrequent(words, k):
    dic = defaultdict()
    # count = 1
    for val in words:
        if val not in dic:
            dic[val] = 1
        else:

            dic[val] += 1


    dic = sorted(dic,key=lambda x: (-dic[x], x))
    print(dic)
    for i in range(0, k):
        print(dic[i][0])

words = ["i", "leetcode","love", "i", "love", "coding"]
k = 2

# topKFrequent(words, k)

def top_k_frequent(words, k):
    hash = collections.Counter(words)
    print(hash)
    res = sorted(hash, key = lambda word:(-hash[word], word))

    print(res[:k])

top_k_frequent(words, k)


'''
collections.Counter(words) 记录每个单词出现的次数
双关键字排序
res = sorted(hash, key = lambda word:(-hash[word], word))
词频倒序排列，Word按字母正序排列
sorted方法默认正序排列

关于sorted排序的多种情况
    1、词频正序，字母正序
    sorted(hash, key = lambda word:(hash[word], word))
    2、词频倒序，字母倒序（revers = True，即将sorted方法修改为倒序排列）
    sorted(hash, key = lambda word:(hash[word], word),reverse = True)
    
    3、词频倒序， 字母正序（本题要求）
    sorted(hash, key=lambda word:(-hash[word], word))

    4、词频正序， 字母倒序
    sorted(hash, key=lambda word:(-hash[word], word), reverse=True)




'''











