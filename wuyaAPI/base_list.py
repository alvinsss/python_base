#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: base_list.py
@time: 2019/01/06
"""

'''1.10 list常用方法的应用 '''
"""'append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
list1 = [1,2,8,4,6,3]
# print(dir(list1))
# help(type(list1))
#insert把元素插入到第几位
# list1.insert(4,5)
#count 在列表3出现几次
# print(list1.count(3))
# index -->索引
# print(list1.index(3))
#pop 默认删除最后一位并打印
# print(list1.pop())
# remove 删除指定的元素,默认从前往后
# print(list1.remove(6))
# print(list1)
#reverse 反转
# print(list1.reverse())
#sort 排序从小到大
# extend 列表合并
list2=['admin','alvin']
# print(list1.extend(list2))
# print(list1,list2)
''' dir 在自动化测试的应用'''
from selenium.webdriver.common.alert import Alert
# print(dir(Alert))
# print(help(type(Alert)))