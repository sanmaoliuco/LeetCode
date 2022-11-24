# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/24 10:02
# @Author : San_mao_liu
# @File : 226_翻转二叉树.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):

    if not root:
        return root

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root



def InvertTree(root):

    if not root:
        return root

    list1 = [root]

    while list1:
        tmp = list1.pop(0)
        tmp.left, tmp.right = tmp.right, tmp.left

        if tmp.left:
            list1.append(tmp.left)

        if tmp.right:
            list1.append(tmp.right)

    return root



def Inver_Tree(root):
    if root:
        root.left, root.right = Inver_Tree(root.right), Inver_Tree(root.left)

    return root

def invert_tree(root):

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root












