# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/10 8:37
# @Author : San_mao_liu
# @File : 排序.py
# @Software: PyCharm

"""
排序算法：
    1、比较类排序
        通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn),
    因此也称为非线性时间比较类排序

    2、非比较类排序
        不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，
    以线性时间运行，因此也称为线性时间非比较类排序

比较类排序：
    交换排序：冒泡排序、快速排序
    插入排序：简单插入排序、希尔排序
    选择排序：简单选择排序、堆排序
    归并排序：二路归并排序、多路归并排序

非比较排序：
    计数排序
    桶排序
    基数排序

初级排序-O(n^2)
    1、选择排序（Selection Sort）
        每次找最小值，然后放到待排序数组的起始位置

    2、插入排序（Insertion Sort）
        从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应
    位置并插入。

    3、冒泡排序（Bubble Sort）
        嵌套循环，每次查看相邻的元素如果逆序，则交换


高级排序-O(nlogn)
    1、快速排序（Quick Sort）
        数组取标杆pivot，将小元素放pivot左边，大元素放右侧，然后依次对右边和右边
    的子数组继续快排；以达到整个序列有序。

    2、归并排序（Merge Sort） - 分治
        1、把长度为n的输入序列分成两个长度为n/2的子序列
        2、对这两个子序列分别采用归并排序
        3、将两个排序好的子序列合并成一个最终的排序序列



归并和快排具有相似性，但步骤顺序相反

归并：先排序左右子数组，然后合并两个有序子数组
快排：先调配出左右子数组，然后对于左右子数组进行排序


堆排序（Heap Sort） 一堆插入O（logN），取最大/小值O(1)
    1、数组元素依次建立小顶堆
    2、依次取堆顶元素，并删除


特殊排序-O(n)

计数排序（Counting Sort）
    计数排序要求输入的数据必须是有确定范围的整数。将输入的数据值转化为键存储在额外
开辟的数组空间中；然后依次把计数大于1 的填充回原数组

桶排序（Bucket Sort）
    桶排序（Bucket Sort）的工作原理：假设输入数据服从均匀分布，将数据分到有限数量
的桶里，每个桶里再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

基数排序（Radix Sort）
    基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位
。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序











"""

# 快排
def quickSort(array, begin, end):
    if end <= begin:
        return
    pivot = partition(array, begin, end)
    quickSort(array, begin, pivot - 1)
    quickSort(array, pivot + 1, end)
    return array

def partition(a, begin, end):
    pivot = end
    counter = begin
    for i in range(begin, end):
        if a[i] < a[pivot]:
            temp = a[counter]
            a[counter] = a[i]
            a[i] = temp
            counter += 1
    temp = a[pivot]
    a[pivot] = a[counter]
    a[counter] = temp
    return counter





# 归并排序

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b [h]:
            c.append(a[j])
            j += 1

        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)

    else:
        for i in a[j:]:
            c.append(i)

    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


array = [1,3,5,6,7,2,12,8]
print(quickSort(array, 0, len(array) - 1))
print(merge_sort(array))

















