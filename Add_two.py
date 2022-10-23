# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/21 20:24
# @Author : San_mao_liu
# @File : Add_two.py
# @Software: PyCharm

class ListNode(object):
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self,data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为data内的数据创建结点，建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return r

    def printList(self,head):
        if head == None:
            return
        node = head
        while node != None:
            print(node.val,end = ' ')
            node = node.next

def addTwoNumbers(l1:ListNode,l2:ListNode)->ListNode:
    if l1 == None:
        return l2

    if l2 == None:
        return l1

    dummy = ListNode(-1)
    p = dummy
    carry = 0

    while l1 and l2 :
        p.next = ListNode((l1.val + l2.val + carry)%10)
        carry = (l1.val + l2.val + carry) // 10
        l1 = l1.next
        l2 = l2.next
        p = p.next


    if l2:
        while l2:
            p.next = ListNode(( l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            p = p.next

    if l1:
        while l1:
            p.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            p = p.next



    if carry == 1:
        p.next = ListNode(1)


    return dummy.next

l = LinkList()
d1= [2,4,3]
d2 = [5,6,4]
l1 = l.initList(d1)
l2 = l.initList(d2)

print(addTwoNumbers(l1,l2))
l.printList(addTwoNumbers(l1,l2))













