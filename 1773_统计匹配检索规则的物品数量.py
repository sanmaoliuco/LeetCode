# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/30 10:55
# @Author : San_mao_liu
# @File : 1773_统计匹配检索规则的物品数量.py
# @Software: PyCharm

def count_Matches(items, ruleKey, ruleValue):
    index = {"type":0, "color":1, "name":2}[ruleKey]
    print(index)
    return sum(item[index] == ruleValue for item in items)


def count_matches(items, ruleKey, ruleValue):
    ans = 0
    index = 0 if ruleKey[0] == 't' else 1 if ruleKey[0] == 'c' else 2
    for item in items:
        if item[index] == ruleValue:
            ans += 1
    return ans

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]

ruleKey = "color"
ruleValue = "silver"

# print(count_Matches(items,ruleKey, ruleValue))
print(count_matches(items, ruleKey, ruleValue))







