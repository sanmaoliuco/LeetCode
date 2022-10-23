# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/30 20:20
# @Author : San_mao_liu
# @File : 深度优先搜索与广度优先搜索.py
# @Software: PyCharm


'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None
'''

# 深度优先搜索
'''
def dfs(node):
    if node in visited:
        # already visited
        return
    visited.add(node)
    # process current node 
    # ... # logic here
    
    dfs(node.left)
    dfs(node.right)
'''

# 多叉树
'''
visited = set()

def dfs(node,visited):
    visited.add(node)
    # process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node,visited)
'''
'''
visited = set()

def dfs(node,visited):
    if node in visited: # terminator
        # already visited 
        return 
    
    visited.add(node)
    
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node,visited)
'''

# 非递归写法
'''
def DFS(self,tree):
    
    if tree.root is None:
        return []
    
    visited , stack = [] , [tree.root]
    
    while stack:
        node = stack.pop()
        visited.append(node)
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        
    # other processing work
    ...
'''

#   广度优先搜索
'''
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
        
    # other processing work 
    
...
'''
'''     
        while True:
            pop_node = queue.pop(0)
            if pop_node.left is None:
                pop_node.left = node
                return
            else:
                queue.append(pop_node.left)

            if pop_node.right is None:
                pop_node.right = node
                return
            else:
                queue.append(pop_node.right)

'''

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None


class Tree:
    def __init__(self):
        self.root = None

    def add_element(self,node_value):
        node = TreeNode(node_value)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while True:
            pop_node = queue.pop(0)
            if not pop_node.left :
                pop_node.left = node
                return
            else:
                queue.append(pop_node.left)

            if pop_node.right is None:
                pop_node.right = node
                return
            else:
                queue.append(pop_node.right)


    def level_oreder(self):

        if not self.root : return []

        queue = [self.root]
        res = []

        while queue:
            res.append([node.val for node in queue])

            l1 = []

            for node in queue:
                if node.left:
                    l1.append(node.left)
                if node.right:
                    l1.append(node.right)
            queue = l1

        return res

    def breadth_travel(self):
        if not self.root:
            return
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.val,end = '  ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)




tree = Tree()

tree.add_element(3)
tree.add_element(9)
tree.add_element(20)
tree.add_element(0)
tree.add_element(0)
tree.add_element(15)
tree.add_element(7)
tree.breadth_travel()


print(tree.level_oreder())


aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2021, 'liner']
aList.extend(bList)
print(aList)


















