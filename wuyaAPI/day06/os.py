#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: os.py
@time: 2019/01/08
"""
import  os
import  sys
# print( os)
#创建文件夹 已经存在返回183 执行cmd net helpmsg 183
# os.mkdir('c:/log')
#修改文件夹名
# os.rename('c:/log','c:/newlog')

#对目录处理 获取当前目录
# print(os.path.dirname(__file__))
#获取文件的上级目录
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

#对day3下的目录的拼接
base_dir = os.path.dirname(__file__)
tar_dir  = os.path.dirname(base_dir)
tar_file = os.path.join(tar_dir,'day3','login.py')
f=open(tar_file, 'r',encoding='UTF-8')
# print (f.read())

# def f1(*args,**kwargs):
#     return  kwargs
# print(f1(name='alvin',age='18'))

'''
python 执行路径搜索：
程序根目录：当前模块的目录
环境变量：安装目录
标准库:安装目录\Lib
三方库：安装目录\Lib\site-packages
'''
# 提示 ModuleNotFoundError: No module named 'day3' 使用sys.path之后导入模块
base_dirday3 = os.path.join(os.path.dirname(os.path.dirname(__file__)),'day3')
sys.path.append(base_dirday3)
# for items in sys.path:
#     print(items)
# from day3.day3Login import  *
# index()
# import day3Login
# day3Login.index()

