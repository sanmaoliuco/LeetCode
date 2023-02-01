# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/2/1 17:39
# @Author : San_mao_liu
# @File : 01web框架.py
# @Software: PyCharm

import socket

server = socket.socket() # TCP 三次握手四次挥手osi七层

server.bind(('127.0.0.1',8080))  # ip协议  以太网协议  arp协议
server.listen(5)

"""
b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n
Connection: keep-alive\r\n
Cache-Control: max-age=0\r\n
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108",
 "Google Chrome";v="108"\r\n
 sec-ch-ua-mobile: ?0\r\n
 sec-ch-ua-platform: "Windows"\r\n
 Upgrade-Insecure-Requests: 1\r\n
 User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) 
 AppleWebKit/537.36 (KHTML, like Gecko) 
 Chrome/108.0.0.0 Safari/537.36\r\n
 Accept: text/html,application/xhtml+xml,application/xml;
 q=0.9,image/avif,image/webp,image/apng,*/*;
 q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
 Sec-Fetch-Site: none\r\n
 Sec-Fetch-Mode: navigate\r\n
 Sec-Fetch-User: ?1\r\n
 Sec-Fetch-Dest: document\r\n
 Accept-Encoding: gzip, deflate, br\r\n
 Accept-Language: zh-CN,zh;q=0.9\r\n\r\n'
"""

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    # print(data)
    data = data.decode('utf-8')
    # 获取字符串中特定的内容  正则  如果字符串有规律也可以考虑用切割
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    current_path = data.split(' ')[1]
    # print(current_path)
    if current_path == '/index':
        # conn.send(b'index heihie')
        with open(r'01myhtml.html','rb') as f:
            conn.send(f.read())
    elif current_path == '/login':
        conn.send(b'login')
    else:
    # 直接忽略favicon.ico
        conn.send(b'hello web')
    conn.close()







