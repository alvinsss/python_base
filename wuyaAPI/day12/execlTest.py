#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: execlTest.py
@time: 2019/01/14
"""
import  xlrd
import  os
import  xlwt
from    xlutils.copy import  copy

def base_dir(filename=None):
    return  os.path.join(os.path.dirname(__file__),filename)

# work = xlrd.open_workbook(base_dir('data.xls'))
# sheet= work.sheet_by_index(0)
# #获取行
# print(sheet.nrows)
# #获取单元格的内容
# print(sheet.cell_value(4,1))

'''xls文件内容的修改,找到对象'''
work =xlrd.open_workbook(base_dir('data.xls'))
old_content=copy(work)
ws = old_content.get_sheet(0)
ws.write(3,2,'avlinnn')
old_content.save(base_dir('data.xls'))

