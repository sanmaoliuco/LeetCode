# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/22 16:37
# @Author : San_mao_liu
# @File : 200_岛屿数量.py
# @Software: PyCharm

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
def numIsland(grid):

    def sink(i, j):

        grid[i][j] = '0'

        for k in range(len(dx)):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and\
                    grid[x][y] == '1':
                sink(x, y)


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    island = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':

                sink(i, j)
                island += 1

    return island





print(numIsland(grid))

# def num_island(grid):
#     def dfs(i, j):
#         grid[i][j] = '0'
#
#         for k in range(len(dx)):
#             x = i + dx[k]
#             y = j + dy[k]
#
#             if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
#                 if grid[x][y] == '1':
#                     dfs(x, y)
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     island = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 dfs(i, j)
#                 island += 1
#
#     return island
#
# print(num_island(grid))















