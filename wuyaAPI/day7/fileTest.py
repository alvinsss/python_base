#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: fileTest.py
@time: 2019/01/09
"""
'''w 写文件'''
# f = open('file.json','w')
# temp = {'name':'alvin',
#         'age':18,
#         'address':'beijing'
#         }
# str1 = str(temp)
# f.write(str1)
# f.close()

'''a 增加'''
# f = open('file.json','a')
# f.write('admin')
# f.close()
'''w 覆盖，不存在自动创建 '''
# f = open('file.json','w')
# f.write("alvin")
# f.close()
'''读文件 ,read()全部内容,read(7)只读7个字符，readlines按行读取，默认第1行'''
# strFileName = '中文.json'
# f = open(strFileName,'r')
# fr = f.read()
# print(type(fr),fr)
# for i in f.readlines():
#     print(i)
# f.close()
'''文件上下文处理 不需要close'''
with open('file.json','w') as f:
    f.write("alvinqatest")

# import json
# json.dump(temp,open('file.json','w'))
