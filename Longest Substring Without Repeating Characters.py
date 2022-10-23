# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/23 20:47
# @Author : San_mao_liu
# @File : Longest Substring Without Repeating Characters.py
# @Software: PyCharm


def length_Longest_Substring(s):
    """
    :param s: str
    :return: int
    """

    if not s:
        return 0

    lookup = list() #滑动窗口
    cur_len = 0   # 记录当前窗口的长度
    max_len = 0    # 记录窗口的最大长度

    for i in s:      # 遍历字符串
        if i in lookup:  # 判断
            index = lookup.index(i)   # i 在窗口中读出序号
            # print(lookup)
            lookup = lookup[index + 1 :]   # 窗口左端右移
            lookup.append(i)
            cur_len -= index    # 更新窗口当前长度

        else:
            lookup.append(i)
            cur_len += 1

        max_len = max(max_len,cur_len)

    return max_len

s = "pwwkew"

def longest(s):
    start = -1
    max = 0
    d = {}

    for i in range(len(s)):
        if s[i] in d and d[s[i]] > start:
            start = d[s[i]]
            d[s[i]] = i

        else:
            d[s[i]] = i   # 往字典中添加键值对
            if i - start > max:
                max = i - start   # i 从0开始计数 但字母出现一次则记为1，故start初始化为-1
                # 字符串存在空集

    return max


# print(length_Longest_Substring(s))
print(longest(s))




























