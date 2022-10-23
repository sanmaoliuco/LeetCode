# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/14 9:36
# @Author : San_mao_liu
# @File : 79_单词搜索.py
# @Software: PyCharm


def exist(board, word):
    row, col = len(board), len(board[0])

    def dfs(x, y, index):
        if board[x][y] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        board[x][y] = "#"

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + di, y + dj
            if 0 <= nx < row and 0 <= ny < col and dfs(nx, ny, index + 1):
                return True

        board[x][y] = word[index]

    for i in range(row):
        for j in range(col):
            if dfs(i, j, 0):
                return True

    return False

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "ABCCED"


print(exist(board, word))









