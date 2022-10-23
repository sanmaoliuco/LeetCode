# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/28 10:59
# @Author : San_mao_liu
# @File : 33_搜索旋转排序数组.py
# @Software: PyCharm


def search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[0] <= nums[mid] and (target > nums[mid]
                                     or target < nums[0]):
            lo = mid + 1

        elif target > nums[mid] and target < nums[0]:
            lo = mid + 1

        else:
            hi = mid

    return lo if lo == hi and nums[lo] == target else -1



def search_(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        if nums[mid] <= nums[len(nums) - 1]:
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1

    return r




nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
print(search_(nums, target))



