#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: base_tuple.py
@time: 2019/01/06
"""
'''1.12 list基础知识元组的讲解 '''
''' 元组不可变，但是元组的元素的数据是可变'''
tuple1 = (1,2,3,4,3,[1,2,3],{'name':'alvin'}) #一个元素一定要加逗号
#count 元素在元组中出现的次数
# print(tuple1.count(3))
#index 元素在元组的中的索引
# print(tuple1.index(2))
'''把元组的列表中由[1,2,3]修改成为[1,2,3,4]'''
print(tuple1[5].insert(3,4))
print(tuple1)
'''把元组的字典name修改qatest'''
print(tuple1[6].get('name'))
# print(type(tuple1[6]))
print(tuple1[6]['name']=='qatest')
print(tuple1)

