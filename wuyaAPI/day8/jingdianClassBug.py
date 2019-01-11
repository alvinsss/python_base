#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: jingdianClassBug.py
@time: 2019/01/09
"""
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(A):
    def show(self):
        print("C")
class D(B,C):
    pass

e = D()
e.show()