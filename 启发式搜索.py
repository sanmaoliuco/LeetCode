# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/30 9:31
# @Author : San_mao_liu
# @File : 启发式搜索.py
# @Software: PyCharm

"""
def BFS(graph, start, end):

    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()  # can we add more intelligence here?
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)

        queue.push(nodes)
"""

# A* search
"""
def AstarSearch(graph, start, end):
    
    pq = collections.priority_queue() # 优先级-》估价函数
    pq.append([start])
    visited.add(start)
    
    while pq:
        node = pq.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
"""

"""
估价函数

启发式函数：h(n),它用来评价哪些结点最有希望的是一个我们要找的结点，h(n)会返回一个非负实数
也可以认为是从结点n的目标结点路径的估计成本

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标

"""

def shorttestPathBinaryMatrix(grid):
    q, n = [(0, 0, 2)], len(grid)   # 起点，终点，步数
    if grid[0][0] or grid[-1][-1]:
        return -1
    elif n <= 2:
        return n

    for i, j, d in q:
        for x, y in [(i - 1,j - 1),(i - 1, j),(i-1,j+1),(i,j-1),
                     (i, j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
            # x,y在坐标系中并且当前位置不为1
            if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                if x == n - 1 and y == n - 1:
                    return d
                q += [(x, y, d + 1)]
                grid[x][y] = 1    # 探过的位置赋值为1,

    return -1
grid = [[0,1],[1,0]]

print(shorttestPathBinaryMatrix(grid))




















