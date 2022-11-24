# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/23 19:28
# @Author : San_mao_liu
# @File : 字典树Trie.py
# @Software: PyCharm

'''
1.字典树的数据结构
2.字典树的核心思想
3.字典树的基本性质

    字典树，即Trie树，又称单词查找树或键树，是一种树形结构。典型应用是用于
    统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。

    优点：最大限度地减少无谓的字符串比较，查询效率比哈希表高

    基本性质：
        1、结点本身不存完整单词
        2、从根节点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串
        3、每个结点的所有子结点路径代表的字符都不相同

    核心思想：
        Trie树的核心思想是空间换时间
        利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的

'''


class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self,word):
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end_of_word] = self.end_of_word

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")


def fib(n):
    if n <= 1:
        return n
    dp = [0 for i in range(n+1)]
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# print(fib(4))
















