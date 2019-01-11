#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: objClass.py
@time: 2019/01/09
"""
S = '''特性方法  这个@property方法不能有形式参数
'''
'''
conn是普通方法
'''
# class Person(object):
#     def conn(self,username,passwd,host,port):
#         pass
#     def f1(self,**kwargs):
#         pass
#
# per1 = Person()
# per1.f1(name='alvin')
# per1.f1()
"""
特性方法：@property不能有形式参数
"""
# class Person(object):
#     @property
#     def getUserId(self):
#         pass
# per = Person()
# per.getUserId

'''
静态方法：直接使用类名来调用 它属于类 对象也可以调用，一般不建议这样做
一个类许多地方需要调用
'''
# class DBconn(object):
#     @staticmethod
#     def mysqlConn(user):
#         pass
# DBconn.mysqlConn('alvin')
# conn = DBconn()
# conn.mysqlConn('alvin')

'''
类方法：直接使用类进行调用 属于类
'''
class Peron(object):
    @classmethod
    def  conn(cls):
        pass
'''
属于类（class名调用，不需要实例化）：
    类属性
    静态方法
    类方法
属于对象（对象名调用的）：
    实例属性
    普通方法
    特性方法
'''

'''
继承:重用已经存在的数据和行为，减少代码的重复编写
子类继承父类所有的实例变量和方法
'''
# class Person(object):
#     china = '地球'
#
# class UsaPerson(Person):
#     pass
#
# per  = UsaPerson()
# per.china

'''实例属性的继承和继承的两种写法
# 子类由于业务需求 需要继承父类的实例属性
# '''
# class Fruit(object):
#     def __init__(self,name):
#         self.name = name
# class Apple(Fruit):
#     def __init__(self,name,brand,color):
#         Fruit.__init__(self,name)
#         self.brand = brand
#         self.color = color
#     def info(self):
#         print ("name:{0},brand:{1},color:{2}".format(self.name,self.brand,self.color))
#
# apple =Apple('苹果','品牌','红色')
# apple.info()
''''
子类由于业务需求 不需要继承父类的实例属性
'''
# class Fruit(object):
#     def __init__(self,name):
#         self.name = name
# class Apple(Fruit):
#     def __init__(self,brand,color):
#         # Fruit.__init__(self,name)
#         self.brand = brand
#         self.color = color
#     def info(self):
#         print (",brand:{0},color:{1}".format(self.brand,self.color))
#
# apple =Apple('品牌','红色')
# apple.info()

'''实例属性的继承和继承的两种写法
'''
class Fruit(object):
    def __init__(self,name):
        self.name = name

class Apple(Fruit):
    def __init__(self,name,brand,color):
        super().__init__(name)
        self.brand = brand
        self.color = color
    def info(self):
        print ("name:{0},brand:{1},color:{2}".format(self.name,self.brand,self.color))

apple =Apple('苹果','品牌','红色')
apple.info()