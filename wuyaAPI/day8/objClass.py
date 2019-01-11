#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: objClass.py
@time: 2019/01/09
"""
'''类是有一些列属性和方法组成的
   对象的创建就是类的实例化的过程
   对象的三个特性：
   1、对象的句柄(id(fun2))，区分不同的对象
   2、属性:
        共有属性
                类属性（共有属性分离出来）
                实例属性
                局部变量
        私有属性
   3、方法
'''
# class f1(object):
#     pass
# fun2 = f1()
# fun1 = f1()
# print(id(fun1),id(fun2))

# class Person(object):
#     #类属性
#     gongTong='地球'
#     #构造函数 类的初始化
#     def   __init__(self,name,age):
#         #实例属性
#         self.name = name
#         self.age  = age
#         # 局部变量，函数编程多些
#         zone = "空间"
#     def  getName(self):
#         return self.name
#     def  getAge(self):
#         return  self.age
#     def setName(self,name):
#         self.name = name
#     def setAge(self,age):
#         self.age = age
#     def info(self):
#         return ('name is :{0}, age is :{1}，来自:{2}'.format(self.getName(),self.getAge(),self.gongTong))
#
# per = Person('alvin',19)
# print(per.getName(),per.getAge())
#
# perlisi = Person('lisi',20)
# print(perlisi.getName(),perlisi.getAge())
# perlisi.setName('lihua')
# perlisi.setAge('21')
# print(perlisi.getName(),perlisi.getAge())
# print(perlisi.info())

# class Person(object):
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#     def info(self):
#         if (self.args == ()):
#             print("没有args",self.kwargs.values())
#         else:
#             print(self.kwargs.values(),self.args)
#
#
# per1 = Person(name='alvin')
# per1.info()
# per2 = Person(name='alvin',age=18)
# per2.info()
# per3 = Person(name='alvin',age=18,addrss="北京")
# per3.info()
# per4 = Person('alvin','21','hlj')
# per4.info()
'''
构造函数
首先一个类，不管是否写构造函数，它都有一个构造函数的
一个类可以有多个构造函数，建议一个类只有一个构造函数
1、初始化属性
'''
class Person(object):
    def __init__(self,name,age):
        print("构造函数")
    def info(self,name):
        self.name = name
        print(self.name)
    def __del__(self):
        print("析构函数")

per = Person('alvin',18)
per.info('alvin')



