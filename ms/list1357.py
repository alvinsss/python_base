#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: list1357.py
@time: 2019/01/11
"""
#  输入5  需要打印[1,3,5,]
def f1(n):
    list1=[]
    for i in range(1,n+1):
        list1.append(i)
        print(i)
    for j in list1:
        if j%2 == 1:
            print(j)

f1(5)
