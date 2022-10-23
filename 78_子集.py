# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/17 9:04
# @Author : San_mao_liu
# @File : 78_子集.py
# @Software: PyCharm


def subsets(nums):
    res = []
    path = []
    def backtrack(nums,statIndex):

        res.append(path[:])
        for i in range(statIndex, len(nums)):
            path.append(nums[i])
            backtrack(nums, i + 1)
            path.pop()

    backtrack(nums, 0)
    return res


def sub_sets(nums):
    res = []
    n = len(nums)

    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])

    helper(0, [])

    return  res



def subSet(nums):
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return  res

def su_sets(nums):
    subsets = [[]]

    for num in nums:
        newsets = []
        for subset in subsets:
            newset = subset + [num]
            newsets.append(newset)
        print(newsets)
        subsets.extend(newsets)
        print(subsets)
    return subsets


# def s_usets(nums):
#     ans = []
#
#     def dfs(ans, nums, li, index):
#         if index == len(nums):
#             ans.append(li)
#             return
#         dfs(ans, nums, li, index + 1)
#         li.append(nums[index])
#         dfs(ans, nums, li, index + 1)
#
#         li.pop(len(li) - 1)
#
#     if not nums:
#         return ans
#     dfs(ans, nums, [], 0)
#
#     return ans




nums = [1, 2, 3]
# print(s_usets(nums))
print(su_sets(nums))
# print(subsets(nums))
# print(sub_sets(nums))
# print(subSet(nums))














