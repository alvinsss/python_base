# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 11:34
# @Author  : alvin
# @File    : 函数装饰器.py
# @Software: PyCharm

def getInfo(func):
    '''
    步骤：
    1、执行f1函数，先执行getinfo，执行getinfo函数时候，把被装饰的函数f1当
    做参数来传递
    2、getinfo函数的单回值会重新赋值
    3、一旦结合了装饰器后，调用f1的函数其实执行的是inner函数的内容，原来
    函数f1被覆盖
    4、被装饰的函数f1重新赋值给装饰器的内层函数inner
    :param func:
    :return:
    '''
    def inner():
        print("python自动化测试")
        func()
    return inner

@getInfo
def f1():
    print("网易云课堂")

def f2():
    print("51CTO课堂")

f1()

#先执行getInfo 再执行f1函数