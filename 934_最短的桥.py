# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/25 11:28
# @Author : San_mao_liu
# @File : 934_最短的桥.py
# @Software: PyCharm

gird = [
    [0,1,0],
    [0,0,0],
    [0,0,1],
]

num_1 = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]


def short_Bridge(grid):
    n, m = len(grid), len(grid[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    st = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                st.append((i, j))
                grid[i][j] = -1
                break
        if st:break

    p = 0
    while p < len(st):
        i,j = st[p]
        for k in range(len(dx)):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                continue
            st.append((x, y))
            grid[x][y] = -1

        p += 1


    for step in range(n * m + 1):
        st2 = []
        for i, j in st:
            for k in range(len(dx)):
                x, y = i + dx[k], j + dy[k]
                if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == -1:
                    continue
                if grid[x][y] == 1:
                    return step

                st2.append((x,y))
                grid[x][y] = -1
        st = st2
    return -1
# print(gird)
# print(short_Bridge(num_1))



def short_br(grid):

    n = len(grid)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    bfs = []

    def dfs(i, j):
        grid[i][j] = -1
        bfs.append((i,j))
        for k in range(len(dx)):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                dfs(x, y)

    def first():
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    return i,j

    step = 0
    dfs(*first())
    while bfs:
        new = []
        for i, j in bfs:
            for k in range(len(dx)):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        return step
                    elif not grid[x][y]:
                        grid[x][y] = -1
                        new.append((x, y))
        step += 1
        bfs = new


print(short_br(num_1))















