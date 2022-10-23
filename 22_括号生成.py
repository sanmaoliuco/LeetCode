# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/4 9:53
# @Author : San_mao_liu
# @File : 22_括号生成.py
# @Software: PyCharm


def _generate(left, right, n, s):
    # terminator
    if left == n and right == n:
        print(s)
        return
    # process current logic: left, right



    # drill down
    if left < n:
        _generate(left + 1, right, n, s + "(")

    if right < left:
        _generate(left, right + 1, n, s + ")")

    # reverse states

# if __name__ == '__main__':
#     _generate(0, 0, 3, "")


def generate(left, right , n, s):
    # terminator
    if left == n and right == n:
        print(s)
        return
    if left < n:
        generate(left + 1, right, n, s + "(")
    if right < left:
        generate(left, right + 1,n, s + ")")


print(generate(0, 0, 3, ""))


def generate_(n):
    if n == 0:
        return []

    res = []
    res.append([None])
    res.append(['()'])
    print(res)

    for i in range(2, n + 1):
        tmp = []
        for j in range(i):
            n1 = res[j]
            n2 = res[i - 1 - j]

            for k1 in n1:
                for k2 in n2:
                    if k1 == None:
                        k1 = ""
                    if k2 == None:
                        k2 = ""

                    el = "(" + k1 + ")" + k2
                    tmp.append(el)

        res.append(tmp)

    return res[n]
# print(generate_(3))
















