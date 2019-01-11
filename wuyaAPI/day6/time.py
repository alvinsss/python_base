#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: time.py
@time: 2019/01/08
"""
import time as t

#时间c
print(int(t.time()))
#获取当前时间
print(t.localtime(t.time()))
#获取时分秒
print(t.strftime("%y-%m-%d %H:%M:%S",t.localtime()))
now = t.strftime("%Y-%m-%d-%H_%M_%S", t.localtime(t.time()))
print (now)
t.sleep(1)