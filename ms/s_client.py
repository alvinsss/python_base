#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: s_client.py
@time: 2019/01/13
"""
import socket
sc = socket.socket()
sc.connect(("127.0.0.1",8002))
while True:
    msg = input(":>>").strip()
    sc.send(msg.encode("utf-8"))
    data_ssend = sc.recv(1024)
    if len(data_ssend) != 0:
        print(data_ssend)
sc.close()