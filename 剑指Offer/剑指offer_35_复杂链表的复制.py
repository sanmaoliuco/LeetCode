# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/30 16:49
# @Author : San_mao_liu
# @File : 剑指offer_35_复杂链表的复制.py
# @Software: PyCharm


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Linklist:
    def __init__(self):
        self.head = None


link_list = Linklist()
node1 = Node(7)
node2 = Node(0)
node3 = Node(2)

link_list.head = node1
node1.next = node2
node1.random = node3

print(link_list.head.next)


def copyRandomList(head):
    cur = head
    dum = pre = Node(0)
    while cur:
        node = Node(cur.val)
        pre.next = node
        cur = cur.next
        pre = node

    return dum.next

def copy_random_list(head):
    if not head:return
    dic = {}

    # 复制各节点，并建立“原节点 -> 新节点”的Map映射
    cur = head
    while cur:
        dic[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    # 构建新节点的next和random指向
    while cur:
        dic[cur].next = dic.get(cur.next)
        dic[cur].random = dic.get(cur.random)
        cur = cur.next
    # 返回新链表的头节点
    return dic[head]







