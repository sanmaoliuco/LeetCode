# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/15 20:56
# @Author : San_mao_liu
# @File : 347_前k个高频元素.py
# @Software: PyCharm

import collections
import heapq
def top_k_frequent(nums,k):

    count = collections.Counter(nums)
    print(count.items())
    print(count)
    for i in count.most_common():
        print(i)

    return [item[0] for item in count.most_common(k)]



def topKFrequent(nums,k):
    count = collections.Counter(nums)
    heap = []
    for key, val in count.items():
        if len(heap) >= k:
            if val > heap[0][0]:
                heapq.heapreplace(heap,(val,key))
        else:
            heapq.heappush(heap, (val, key))
    return [item[1] for item in heap]



nums = [1,1,2,2,1,3,4,5]
# print(top_k_frequent(nums,2))
print(topKFrequent(nums,2))







