# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/30 15:31
# @Author : San_mao_liu
# @File : 剑指Offer_24_反转链表.py
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList:
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

    s = []
    while link_list.head:
        s.append(link_list.head.val)
        link_list.head = link_list.head.next
    print(s)

    def reverseList(head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev.val

    def reverse_list(head):
        if head == None or head.next == None:
            return head

        new_head = reverse_list(head.next)
        head.next.next = head
        head.next = None

        return new_head.next.val

    print(reverseList(node1))
    print(reverse_list(node1))






