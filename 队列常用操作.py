# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/28 17:39
# @Author : San_mao_liu
# @File : 队列常用操作.py
# @Software: PyCharm


from collections import deque

class Test:
    def test(self):
        # create a queue
        queue = deque()

        # Add element
        # Time Complexity:O(1)

        queue.append(1)
        queue.append(2)
        queue.append(3)

        print(queue)

        # Get the head of the queue
        # Time Complexity:O(1)
        temp1 = queue[0]

        print(temp1)

        #Remove the head of the queue
        # Time Complexity :O(1)
        temp2 = queue.popleft()

        print(temp2)

        print(queue)



        while len(queue) != 0:
            temp = queue.popleft()
            print(temp)


if __name__ == '__main__':
    test = Test()
    test.test()






















