# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/8 9:08
# @Author : San_mao_liu
# @File : 链表.py
# @Software: PyCharm

"""
链表是由一系列节点组成的元素集合，每个节点包含两部分，数据域item和指向下一个节点的
指针next。通过节点之间的相互连接，最终串联成一个链表
"""

'''
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

a =Node(1)
b =Node(2)
c =Node(3)

a.next = b
b.next = c
print(a.next.next.item)

'''

'''
创建链表
头插法
尾插法
'''
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

# 头插法
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

# 尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


# 链表的插入
def linklist_insert(li,p):
    create_linklist_head(li)
    head = Node(li[0])
    # print(head.item)
    tail = Node(li[len(li) - 1])
    # print(tail.next)
    # if not isinstance(p,Node):
    #     p = Node(p)
    #     print(p.item)
    # p = Node(p)
    # if  head is None:
    #     # p = Node(p)
    #     p.next = head
    #     head = p
    # else:
    #     tail.next = p.item
    # p.next = tail
    # return
    p = Node(p)
    p.next = head.next
    head.next = p

    return head


def print_linklist(lk):
    while lk:
        print(lk.item , end=',')
        lk = lk.next

lk = [1,2,3]
# lo = create_linklist_tail([1,2,3])
# print_linklist(lk)
create_linklist_head(lk)

print_linklist(linklist_insert(lk,4))
# print('\n')
# print_linklist(lo)



















