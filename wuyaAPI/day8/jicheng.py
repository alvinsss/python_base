#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: jicheng.py
@time: 2019/01/09
"""

'''方法的继承
子类为啥重写父类的方法：子类有自己的特性
当子类重写父类的方法后，对子类进行实例化后，子类调用的
方法（父类，子类都存在）

单个类继承的原则
1从上到下，子类继承父类，但子类没有重写父类的方法，那么
子类实例化后，调用方法是直接调用父类的方法
2从下到上的原则：子类继承父类，但子类重写父类的方法，那么
子类实例化后，调用方法是子类的方法（优先考虑自己）

'''
class  Fruit(object):
    def eat(self):
        print("吃的")
class ChinaApple(Fruit):
    def __init__(self,color):
        self.color =color
    def eat(self):
        print("ChinaApple颜色是红色".format(self.color))

class UsaApple(ChinaApple):
    def eat(self):
        print("Use Eat")

apple =UsaApple('红色')
apple.eat()