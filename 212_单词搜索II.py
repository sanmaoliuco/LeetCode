# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/13 17:10
# @Author : San_mao_liu
# @File : 212_单词搜索II.py
# @Software: PyCharm

import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
END_OF_WORD = "#"

def findWords(board, words):
    if not board or not board[0]: return []
    if not words: return []
    result = set()

    # 构建Trie
    root = collections.defaultdict()
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, collections.defaultdict())

        node[END_OF_WORD] = END_OF_WORD



    def _dfs(board, i, j, cur_word, cur_dict):
        # terminator
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y, = i + dx[k], j + dy[k]
            if 0 <= x < m and 0 <= y < n and board[x][y] != '@' \
                    and board[x][y] in cur_dict:
                _dfs(board, x, y, cur_word, cur_dict)

        board[i][j] = tmp

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] in root:
                _dfs(board, i, j, "", root)

    return list(result)


board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]

words = ["oath","pea","eat","rain"]


print(findWords(board, words))
























