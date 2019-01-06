#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: base.py
@time: 2019/01/06
"""
'''1.6  Python3编码解码的讲解,3内部编码自动转换,默认unicode'''
# s= "海林"
# print(type(s))
# s1 = s.encode()
# s2 = s1.decode()
# print(type(s1),"s1=",s1,"s2=",s2)

'''1.7 str常用方法的应用 '''
# a = 3
# b = '3'
# print( type(a),type(b))
str1= "ASFDasd"
# print(dir(str1)) #查看对字符串操作的方法
# print(help(type(str1))) #查看类的源码
"""'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""
# print("D在字符串的索引第几位：",str1.index('D'))
# print("小写转大写：",str1.upper())
# print("大写转小写：",str1.lower())
# print("字符串是以A开始:",str1.startswith('A'))
# print("字符串是以d结束:",str1.endswith('d'))
# print("字符串-->列表:",str1.split('D') )
# print("字符串的替换：",str1.replace('asd','ASD')) #查看方法，鼠标放函数按Ctrl 左键
# print("F在第",str1.find('F'),"位")
list1 = '字符串-->列表:',str1.split('D')

'''1.8 单引号与双引号的区别和应用 '''
# 1.在单引号中不能使用单引号
# 2.在双引号中不能使用双引号
# 3.在单引号中可以使用双引号
# 4.在双引号中可以使用单引号
# str3 = "'b'"
# str4 = "\"a\""
# print(str3,str4)

'''1.9 字符串格式化的讲解 '''
# name = 'alvin'
# age  = 18
# address = "beijing"
# print('my name is %s,age is %d,addres is %s'%(name,age,address)) #推荐
# print('my name is {0},age is {1},addres is {2}'.format(name,age,address))
# print('my name is {:s},age is {:d},addres is {:s}'.format(name,age,address))
# print('my name is {name},age is {age},addres is {address}'.format(name=name,age=age,address=address))


