#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: csvAction.py
@time: 2019/01/15
"""
import  csv
'''读出列表格式'''
def readCSVlist():
    with open('data.csv','r') as f:
        reader = csv.reader(f)
        #跳过表头
        next(reader)
        data = [i for i in reader]
        print(data[0])


def  readCSVdict():
    with open('data.csv','r') as f:
        reader = csv.DictReader(f)
        for i in reader:
            # print(dict(i))
            dict1 = dict(i)['测试用例']
            print(dict(i)['测试用例'])
            # print(dict1[0])
# readCSVlist()
readCSVdict()