#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: s_server.py
@time: 2019/01/13
"""
import socket
import os
s = socket.socket()
s.bind(("127.0.0.1",8002))
s.listen()
while True:
    conn ,addr = s.accept()
    print("client is online")
    while True:
        data = conn.recv(1024)
        print(str(data))
        if not data:
            print("client is lose")
        conn.send(data.upper())

        if str(data,encoding='utf-8') == "exit":
            print("clien is send exit!")
            os._exit(1)

s.close()