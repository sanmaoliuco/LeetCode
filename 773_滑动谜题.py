# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/30 10:19
# @Author : San_mao_liu
# @File : 773_滑动谜题.py
# @Software: PyCharm


moves = {
    0:[1,3],
    1:[0,2,4],
    2:[1,5],
    3:[0,4],
    4:[1,3,5],
    5:[2,4]
}

def slidingPuzzle(self,board):
    used = set()
    cnt = 0
    s = "".join(str(c) for row in board for c in row)
    q = [(s,s.index("0"))]
    while q:
        new = []
        for s, i in q:
            used.add(s)
            if s == "123450":
                return  cnt

            arr = [c for c in s ]
            for move in moves[i]:
                new_arr = arr[:]
                new_arr[i], new_arr[move] = new_arr[move],new_arr[i]
                new_s = "".join(new_arr)
                if new_s not in used:
                    new.append((new_s,move))
        cnt += 1
        q = new
    return  -1


def sliding_puzzle(board):
    board = board[0] + board[1]
    moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (4, 2)]

    q, visited = [(tuple(board), board.index(0), 0)], set()

    while q:
        state, now, step = q.pop(0)
        if state == (1, 2, 3, 4, 5, 0):
            return step

        for next in moves[now]:
            _state = list(state)
            _state[next], _state[now] = _state[now], _state[next]
            _state = tuple(_state)

            if _state not in visited:
                q.append((_state, next, step + 1))

        visited.add(state)

    return -1

board = [[4, 1, 2], [5, 0, 3]]
print(sliding_puzzle(board))




















