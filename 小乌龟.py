# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/18 17:32
# @Author : San_mao_liu
# @File : 小乌龟.py
# @Software: PyCharm


# from turtle import *
# from time import *
# import turtle
# t = Turtle()
# t.pensize(2)
# turtle.bgcolor("black")
# colors = ["red", "yellow", 'purple', 'blue']
# t._tracer(False)
# for x in range(400):
#     t.forward(2*x)
#     t.color(colors[x % 4])
#     t.left(91)
# t._tracer(True)
# done()




class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None


class Tree:
    def __init__(self):
        self.root = None

    def add_element(self,node_val):
        node = TreeNode(node_val)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]

        while True:
            pop_node = queue.pop(0)
            if not pop_node.left:
                pop_node.left = node
                return
            else:
                queue.append(pop_node.left)

            if not pop_node.right:
                pop_node.right = node
                return
            else:
                queue.append(pop_node.right)

    def breadth_travel(self):
        if not self.root:
            return
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.val,end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # def preorderTraversal(self,root):
    #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []




tree = Tree()
tree.add_element(1)
tree.add_element(4)
tree.add_element(8)
tree.add_element(6)
tree.add_element(5)


tree.breadth_travel()
root = [1,3,4,5]

























