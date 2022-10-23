# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/4 8:27
# @Author : San_mao_liu
# @File : AVL树和红黑树.py
# @Software: PyCharm

'''
def preorder (self,root):

    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)


def inorder(self,root):

    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)


def postorder(self,root):

    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)

'''

"""

二叉搜索树  Binary Search Tree
二叉搜索树，也称有序二叉树（Ordered Binary Tree）、排序二叉树（Sorted Binary Tree）
,是指一棵空树或者具有下列性质的二叉树：
    1.左子树上所有结点的值均小于它的根结点的值
    2.右子树上所有结点的值均大于它根结点的值
    3.以此类推：左、右子树也分别为二叉查找树。（这就是重复性）
    
    中序遍历：升序排列

二叉搜索树的查询效率只与高度有关与结点个数无关

AVL树：
    Balance Factor(平衡因子)：
        是它的左子树的高度减去它的右子树的高度（有时相反）
        balance factor = {-1,0,1}
    
    通过旋转操作来进行平衡
        左旋
        右旋
        左右旋
        右左旋

    总结:
        1、平衡二叉树
        2、每个结点存balance factor = {-1,0,1}
        3、四种旋转操作
        
    不足：结点需要存储额外信息，且调整次数频繁



"""

"""
红黑树
    红黑树是一种近似平衡的二叉树（Binary Search Tree），它能够确保任何一个结点的
    左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉搜索树：
        
        每个结点要么是红色，要么是黑色
        根结点是黑色
        每个叶结点（NIL结点，空结点）是黑色的
        不能有相邻的两个红色结点
        从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点
        
    关键性质：
        从根到叶子的最长的可能路劲不多于最短的可能路劲的两倍长


"""

'''
对比
    1、 AVL trees provide faster lookups than Red Black Trees because
    they are more strictly balanced 
    
    2、 Red Black Trees provide faster insertion and removal operations
    than AVL trees as fewer rotations are done due to relatively relaxed
    balancing
    
    3、 AVL trees store balance factors or heights with each node,thus 
    requires storage for an integer per node whereas Red Black Tree requires
    only 1 bit of information per node.
    
    4、 Red Black Trees are used in most of the language libraries like 
    map,multimap,multiset in C++ whereas AVL trees are used in databases 
    where faster retrievals are required.
    

'''













