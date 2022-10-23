# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/25 9:03
# @Author : San_mao_liu
# @File : 638_大礼包.py
# @Software: PyCharm

from functools import lru_cache

def shopping_Offers(price,special,needs):
    n = len(price)
    filter_special = []
    for sp in special:
        if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
            filter_special.append(sp)


    @lru_cache()
    def dfs(cur_need):
        min_price = sum(need * price[i] for i , need in enumerate(cur_need))
        for cur_special in filter_special:
            special_price = cur_special[-1]
            nxt_need = []

            for i in range(n):
                if cur_special[i] > cur_need[i]:
                    break
                nxt_need.append(cur_need[i] - cur_special[i])

            if len(nxt_need) == n:
                min_price = min(min_price, dfs(tuple(nxt_need)) + special_price)

        return min_price

    return dfs(tuple(needs))



price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(shopping_Offers(price,special,needs))





















