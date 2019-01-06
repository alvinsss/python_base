#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: def02.py
@time: 2019/01/06
"""
''' 
2.1 动态参数的讲解
*args -->元组 
**kwargs -> 字典
'''
def  f2(*args):
    print(args,type(args))
f2()

def f3(**kwargs):
    print(kwargs,type(kwargs))
f3()

def f4(name,age,sex,**kwargs):
    print('用户信息:',name,age,sex,kwargs)

f4('alvin',18,'boy')
f4('alvin',18,'boy',code='222222',address='beijing')

def f5(*args,**kwargs):
    print(args,kwargs)
f5()
f5(2)

def f6(name):
    print(name)
# f6()
# f6(2)
# f6('admin')
# f6(['a','b'])
# f6(adress='beijin')
# f6((a,b))
# f6({'name':'alvin','age':18})

# f5()
f5(2)
f5('admin')
f5(['a','b'])
f5(adress='beijin')
f5(('a','b'))
f5({'name':'alvin','age':18})
