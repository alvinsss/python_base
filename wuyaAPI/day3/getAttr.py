#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: getAttr.py
@time: 2019/01/07
"""
import login
# 通过__import__导入模块放在一个对象中
# f = __import__('login')
# #通过对象找login模块的index的字符串并调用
# print(f.index())

# import  login
# #调用login模块（文件）的logout函数
# f= getattr(login,'logout')
# print(f())

#如何找到Person中的info方法并调用
# if hasattr(obj,'info'):
#     f = getattr(obj,'info')
#     print(f())
# else:
#     print("没有找到！")
# obj =  login.Person()
# f = setattr(obj,'exit','this is exit method')
# f2 = hasattr(obj,'exit')
# print("hasattr 之后的结果:",f2)
#
# f3=delattr(obj,'exit')
# print("delattr 之后的结果:",f3)
# f4= getattr(obj,'info')
# print(f4())

#login模块的str1变量
# fn1= hasattr(login,'str1')
# print(fn1)
# fn2= delattr(login,'str1')
# print(fn2)
# fn3= hasattr(login,'str1')
# print("delattr 之后：",fn3)
# fn4= setattr(login,'str2','hello world')
# fn5 = hasattr(login,'str2')
# print(fn5)
url = input("输入路由地址(tar_models/tar_fun):")
print(url)
tar_models,tar_fun = url.split('/')#login/index
print(tar_models,tar_fun)
m=__import__(tar_models)
if hasattr(m,tar_fun):
    tar_fun = getattr(m,tar_fun)
    tar_fun()
else:
    print("Not Found 404 Page")