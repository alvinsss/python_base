#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: jichengduo.py
@time: 2019/01/09
"""
'''
多个类继承，从左到右,父类必须统一层级的
'''
class Person(object):
    def eat(self):
        print("人吃饭")
class Monther(Person):
    def eat(self):
        print("吃菜")
    def dirv1(self):
        print("Monther dirv1")

class Father(Person):
    def eat(self):
        print("F 吃水果")

class Son(Father,Monther):
    pass

son=Son()
son.eat()
son.dirv1()