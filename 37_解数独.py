# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/6 21:22
# @Author : San_mao_liu
# @File : 37_解数独.py
# @Software: PyCharm


def solveSudoku(board):
    row = [set(range(1,10)) for _ in range(9)]
    col = [set(range(1,10)) for _ in range(9)]
    block = [set(range(1,10)) for _ in range(9)]

    empty = []

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                val = int(board[i][j])
                row[i].remove(val)
                col[j].remove(val)
                block[i//3 * 3 + j // 3].remove(val)
            else:
                empty.append((i,j))

    def backtrack(iter = 0):
        if iter == len(empty):
            return True

        i, j = empty[iter]
        b = i//3 * 3 + j // 3

        for val in row[i] & col[j] & block[b]:
            row[i].remove(val)
            col[j].remove(val)
            block[b].remove(val)

            board[i][j] = str(val)

            if backtrack(iter+1):
                return True
            row[i].add(val)
            col[j].add(val)
            block[b].add(val)

        return False


    backtrack()

    return board

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(solveSudoku(board))
































