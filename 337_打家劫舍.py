# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/3 10:46
# @Author : San_mao_liu
# @File : 337_打家劫舍.py
# @Software: PyCharm



class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if self.root == None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left == None:
                cur.left = node
                return
            else:
                queue.append(cur.left)
            if cur.right == None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    # 后序遍历
    # def post_order(self, node):
    #     if node == None:
    #         return
    #     self.post_order(node.left)
    #     self.post_order(node.right)
    #     print(node.val, end='  ')

    def rob(self, Node):
        if Node is None:
            return 0
        if Node.left == None and Node.right == None:
            return Node.val

        val1 = Node.val
        if Node.left:
            val1 += self.rob(Node.left.left) + self.rob(Node.left.right)
        if Node.right:
            val1 += self.rob(Node.right.right) + self.rob(Node.right.left)

        val2 = self.rob(Node.left) + self.rob(Node.right)

        print(max(val1, val2))

if __name__ == '__main__':
    t = Tree()
    t.add(3)
    t.add(2)
    t.add(3)
    t.add(0)
    t.add(3)
    t.add(0)
    t.add(1)
    t.rob(t.root)
    # t.post_order(t.root)


