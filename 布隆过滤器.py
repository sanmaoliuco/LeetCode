# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/8 8:52
# @Author : San_mao_liu
# @File : 布隆过滤器.py
# @Software: PyCharm


"""
Bloom Filter
一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否
在一个集合中

优点是空间效率和查询时间都远远超过一般的算法
缺点是有一定的误识别率和删除困难


"""

# 布隆过滤器的实现
from bitarray import bitarray
import mmh3

class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self,s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if  self.bit_array[result] == 0:
                return "Nope"
            return "Probably"

bf = BloomFilter(500000, 7)
bf.add("dantezhao")
print(bf.lookup("dantezhao"))
print(bf.lookup("yyj"))

















