# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 10:32
# @Author : San_mao_liu
# @File : 堆操作.py
# @Software: PyCharm

import heapq

class Test:
    def test(self):

        minheap = []
        heapq.heapify(minheap)

        heapq.heappush(minheap,10)
        heapq.heappush(minheap,8)
        heapq.heappush(minheap,9)
        heapq.heappush(minheap,2)
        heapq.heappush(minheap,1)
        heapq.heappush(minheap,11)

        print(minheap)

        print(minheap[0])

        heapq.heappop(minheap)

        len(minheap)

        while len(minheap) != 0:
            print(heapq.heappop(minheap))

if __name__ == '__main__':
    test = Test()
    test.test()









