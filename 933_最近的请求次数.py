# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/28 17:58
# @Author : San_mao_liu
# @File : 933_最近的请求次数.py
# @Software: PyCharm


from collections import deque

class Test:
    def test(self):
        # create a queue
        self.queue = deque()

    def ping(self,t):
        self.queue.append(t)
        while len(self.queue) > 0 and t - self.queue[0] > 3000:
            self.queue.popleft()

        return len(self.queue)

if __name__ == '__main__':
    test = Test()
    # t = [[], [1], [100], [3001], [3002]]
    test.test()
    test.ping(1)
    test.ping(100)
    test.ping(3001)
    print(test.ping(3002))













