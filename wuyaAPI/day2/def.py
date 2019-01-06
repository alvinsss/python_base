#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: def.py
@time: 2019/01/06
"""
print("def")
'''
函数是一段可以重复调用的代码 通过输入的参数，返回对应的结果
1、函数调用的时候，实际参数的值的顺序与形式参数的顺序一一对应
2、当函数的调用的时候，指定了形式参数的实际参数 这个时候并不是一一对应，而是根据指定的值进行的

函数的返回值：
1、一个函数它有返回值的
2、当一个函数没return的时候，它的返回值是None
3、当一个函数return的时候它的返回值是return 后面的表达式或值

函数的意义：函数的返回值为了给另外的一个函数一个请求的参数而已
'''
def add(a,b):
    print(a+b)
    c= a+b
    return c
add('alvin','hailin')
print( add(b=3,a=2) )

def info (name,age,address,sex):
    print("name:{0},age:{1},address:{2},sex:{3}".format(name,age,address,sex))
    # print("name:{:s},age:{:d},address:{:s},sex:{:s}".format(name,age,address,sex))
    print(name,age,address,sex)

# info('alvin','18','beijing','boy')

def login(username='alvin',passwd='admin'):
    if username=='alvin' and passwd == 'admin':
        print('sucess')
        return  'tokenxxxxxxxxxxxxxx'
    else:
        print('fail login ')
        return 'fail login'

def userInfo(token):
    '''查看用户信息'''
    if token == 'tokenxxxxxxxxxxxxxx':
        print('information order...')
    else:
        print('logout')

login('hailin','admin')
gettoken = login('alvin','admin')
userInfo(gettoken)