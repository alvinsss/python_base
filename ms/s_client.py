
#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: s_client.py
@time: 2019/01/11
"""

import socket

client = socket.socket()
client.connect(('localhost', 7000))  # 连接服务器

while True:
    msg = input(">>:").strip()
    if len(msg) == 0: continue
    client.send(msg.encode())  # 发送数据
    data = client.recv(1024)  # 接收数据
    print("返回数据:", data.decode())
