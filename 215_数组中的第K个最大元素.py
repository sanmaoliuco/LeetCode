# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 10:46
# @Author : San_mao_liu
# @File : 215_数组中的第K个最大元素.py
# @Software: PyCharm

import heapq

def findKthLargest(nums, k):
    maxheap = []
    heapq.heapify(maxheap)

    while len(nums) != 0:
        heapq.heappush(maxheap, nums.pop() * (-1))

    print(maxheap)
    print(maxheap[k-1] * (-1))

# nums = [3,2,3,1,2,4,5,5,6]
# nums = nums.sort()
# print(findKthLargest(nums,k=4))



# 快速排序

# def quick_sort(nums, start, end):
#     if start >= end:
#         return
#
#     mid_value = nums[start]
#     low = start
#     high = end
#
#     while low < high:
#         while low < high and nums[high] > mid_value:
#             high -= 1
#
#         nums[low] = nums[high]
#
#         while low < high and nums[low] <= mid_value:
#             low += 1
#         nums[high] = nums[low]
#
#     nums[low] = mid_value
#
#     quick_sort(nums, start, low-1)
#     quick_sort(nums, low + 1, end)
#
# if __name__ == '__main__':
#     nums = [7,1,2,5,6,9,3,8]
#     quick_sort(nums, 0, len(nums) - 1)
#     print(nums)

class Solution:
    def findKthLargest(self, nums, k) :
        k = len(nums) - k
        low = 0
        high = len(nums) - 1
        while low <= high:
            p = self.quick_sort(nums, low, high)
            if k < p:
                high = p - 1
            elif k > p:
                low = p + 1
            else:
                return nums[p]
        return -1

    def quick_sort(self,nums, low, high):

        mid_value = nums[low]

        while low < high:
            while low < high and nums[high] >= mid_value:
                high -= 1

            nums[low] = nums[high]

            while low < high and nums[low] <= mid_value:
                low += 1
            nums[high] = nums[low]

        nums[low] = mid_value

        return low

    # return nums[k]

if __name__ == '__main__':
    nums = [7,1,2,5,6,9,3,8]
    k = 4
    demo = Solution()
    print(demo.findKthLargest(nums,k))











