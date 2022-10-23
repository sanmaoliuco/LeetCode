# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/25 15:53
# @Author : San_mao_liu
# @File : 433_最小基因变化.py
# @Software: PyCharm


def minMutation(start, end, bank):
    hash_map = ['A', 'G', 'T', 'C']
    queue = [(start, 0)]

    while queue:
        word, step = queue.pop(0)
        if word == end:
            return step

        for i in range(len(word)):
            for p in hash_map:
                tmp = word[:i] + p + word[i + 1:]
                if tmp in bank:
                    bank.remove(tmp)
                    queue.append((tmp, step + 1))

    return -1



start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(minMutation(start, end, bank))











