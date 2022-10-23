# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/6 10:12
# @Author : San_mao_liu
# @File : 36_有效的数独.py
# @Software: PyCharm

from collections import defaultdict
def is_valid_sudoku(board):
    row = defaultdict(set)
    col = defaultdict(set)
    box = defaultdict(set)

    for i in range(9):
        for j in range(9):
            cur = board[i][j]

            if cur == '.':
                continue
            if cur not in row[i]:
                row[i].add(cur)
            else:
                return False
            if cur not in col[j]:
                col[j].add(cur)
            else:
                return False
            k = i // 3 * 3 + j // 3
            if cur not in box[k]:
                box[k].add(cur)
            else:
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(is_valid_sudoku(board))






















