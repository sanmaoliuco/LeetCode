# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/1 18:17
# @Author : San_mao_liu
# @File : 02基于wsgiref模块.py
# @Software: PyCharm


from wsgiref.simple_server import make_server

def run(env, response):
    """

    :param env: 请求相关的所有数据
    :param response: 响应相关的所有数据
    :return: 返回给浏览器数据
    """
    # print(env)   # 大字典  wsgiref 模块帮你处理好http数据
    response('200 OK', [])  # 响应首行 响应头
    # 从env中取出
    current_path = env.get('PATH_INFO')
    if current_path == '/index':
        return [b'index']
    elif current_path == '/login':
        return [b'login']



    # return [b'hello wsgiref']
    return [b'404 error']
if __name__ == '__main__':

    server = make_server('127.0.0.1',8080,run)
    """
    会实时监听127.0.0.1:8080地址 只要有客户端来了都会交给
    run函数处理（加括号触发run函数的运行）
    
    flask 启动源码
        make_server('127.0.0.1',8080,obj)
        触发obj，__call__
    """
    server.serve_forever()  # 启动服务端





