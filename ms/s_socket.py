#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: socket.py
@time: 2019/01/11
"""

from socket import *
import  socket
'''
服务器端的基本流程：
1.初始化socket（）
2.使用bind()绑定ip和端口号
3使用listen()监听消息
4.获取客户端的套接字地址accept()
5.使用recv()接收数据，send()发送数据与客户端进行交互

客户端的基本流程：
1.初始化socket（）
2.使用ip和端口号connect()连接服务器
3.使用recv()接收数据，send()发送数据与服务器进行交互

在Python的Socket无外乎就两个主要方法，一个是发送数据的send()和接收数据的recv()，所以想要做好交互，
只要做好两边接收和发送的操作即可，但需要注意的是，两边的send和recv都是需要正确的对应好，不然就会使
客户端或者服务器端出现挂起状态。
'''
server = socket.socket(socket.AF_INET, socket.STREAM)
server.bind(('localhost', 6969))  # 绑定ip和端口

server.listen(5)  # 监听，设置最大数量是5
print("开始等待接受客户端数据----")
while True:
    conn, addr = server.accept()  # 获取客户端地址
    print(conn, addr)
    print("客户端来数据了")
    while True:
        data = conn.recv(1024)  # 接收数据
        print("接受的数据：", data)
        if not data:
            print("client has lost")
            break
        conn.send(data.upper())  # 返回数据

serve.close()

