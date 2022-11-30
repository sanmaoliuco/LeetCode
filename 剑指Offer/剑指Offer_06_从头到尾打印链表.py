# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/30 14:54
# @Author : San_mao_liu
# @File : 剑指Offer_06_从头到尾打印链表.py
# @Software: PyCharm


# 定义结点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    link_list = SingleLinkList()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    link_list.head = node1
    node1.next = node2
    node2.next = node3

    # print(link_list.head.val)
    # print(link_list.head.next.val)
    s = []
    while link_list.head:
        s.append(link_list.head.val)
        link_list.head = link_list.head.next
    # print(s)

    # 复制链表
    def copy_link_list(head):
        cur = head
        dum = pre = ListNode(0)
        while cur:
            node = ListNode(cur.val)   # 复制节点cur
            pre.next = node            # 新链表的前驱节点 -> 当前节点
            cur = cur.next             # 遍历下一节点
            pre = node                 # 保存当前节点

        return dum.next.val

    print(copy_link_list(node1))

    # 递归
    def reversePrint(head):

        return reversePrint(head.next) + [head.val] if head else []

    # print(reversePrint(node1))

    # 辅助栈
    def reverse_print(head):
        s = []
        while head:
            s.append(head.val)
            head = head.next

        return s[::-1]

    # print(reverse_print(node1))





