# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/3 17:31
# @Author : San_mao_liu
# @File : Hash_map.py
# @Software: PyCharm


class Test:
    def test(self):
        hashTable = [''] * 4

        mapping = {}

        hashTable[1] = 'a'
        hashTable[2] = 'b'
        hashTable[3] = 'c'

        mapping[1] = 'a'
        mapping[2] = 'b'
        mapping[3] = 'c'

        # Update element
        hashTable[1] = 'bi'
        mapping[1] = 'bi'

        # Remove element
        hashTable[1] = ''
        mapping.pop(1)


if __name__ == '__main__':
    ts = Test()
    ts.test()













