# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/25 10:59
# @Author : San_mao_liu
# @File : 98_验证二叉搜索树.py
# @Software: PyCharm

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class solution:
    def isValidBST(self, root):
        output = []

        self.inorder(root, output)
        print(output)
        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return  False

        return True

    def inorder(self,root, output):
        if not root:
            return

        self.inorder(root.left,output)
        output.append(root.val)
        self.inorder(root.right, output)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

op = solution()
op.isValidBST(root)

















