# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/7 10:13
# @Author : San_mao_liu
# @File : 705_设计哈希表.py
# @Software: PyCharm


# class MyHashSet:
#
#     def __init__(self):
#         self.hashset = [[] for _ in range(1000)]
#
#
#     def add(self, key: int) -> None:
#         if not self.hashset[key % 1000]:
#             self.hashset[key % 1000] = [] * 1001
#         self.hashset[key % 1000][key // 1000] = True
#
#
#     def remove(self, key: int) -> None:
#         if self.hashset[key % 1000]:
#             self.hashset[key % 1000][key // 1000] = False
#
#     def contains(self, key: int) -> bool:
#         return (self.hashset[key % 1000] != []) and (self.hashset[key % 1000][key // 1000])
#
#
#
# if __name__ == '__main__':
#     myhashset = MyHashSet()
#     myhashset.add(999999)
#     myhashset.contains(999999)
#     print(myhashset.hashset)


class MyHashSet:

    def __init__(self):
        # self.buckets = 1000
        # self.itemsPerBucket = 1001
        self.table = [[] for _ in range(1000)]

    # def hash(self, key):
    #     return key % 1000
    #
    # def pos(self, key):
    #     return key // 1000

    def add(self, key):
        # hashkey = self.hash(key)
        if not self.table[key % 1000]:
            self.table[key % 1000] = [0] * 1001
        self.table[key % 1000][key // 1000] = 1

    def remove(self, key):
        # hashkey = self.hash(key)
        if self.table[key % 1000]:
            self.table[key % 1000][key // 1000] = 0

    def contains(self, key):
        # hashkey = self.hash(key)
        return (self.table[key % 1000] != []) and (self.table[key % 1000][key // 1000] == 1)



if __name__ == '__main__':
    myhashset = MyHashSet()
    myhashset.add(1000000)
    myhashset.contains(1000000)
    print(myhashset.table)




