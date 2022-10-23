# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/5 20:20
# @Author : San_mao_liu
# @File : 高级搜索.py
# @Software: PyCharm


'''

1、剪枝
2、双向BFS
3、启发式搜索（A*）


初级搜索：
    1、朴素搜索
    2、优化方式：不重复（fibonacci）、剪枝（生成括号问题）
    3、搜索方向：
        DFS：depth first search 深度优先搜索
        BFS：breadth first search 广度优先搜索

        双向搜索、启发式搜索


'''
'''
# dfs代码-递归写法

visited = set()

def dfs(node,visited):
    if node in visited:  # terminator
    # already visited
        return 
    
    visited.add(node)
    # process current node here
    
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node,visited)
            
# DFS代码-非递归写法            
    
            
def DFS(self,tree):
    
    if tree.root is None:
        return 
    
    visited,stack = [],[tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        
    # other processing work
    
'''

'''
# BFS 代码
def BFS(graph,start,end):
    
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes) 
'''

'''
回溯法
回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它
通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是
上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
    找到一个可能存在的正确的答案
    在尝试了所有可能的分步方法后宣告该问题没有答案
  在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算
    
'''




























