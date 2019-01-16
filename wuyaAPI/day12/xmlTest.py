#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: xmlTest.py
@time: 2019/01/16
"""
import  xml.dom.minidom

def getXMLalone(key=None):
    '''获取单节点数据'''
    xmlFile = xml.dom.minidom.parse('data.xml')
    data    = xmlFile.documentElement
    itemList = data.getElementsByTagName(key)
    item=itemList[0]
    print(item.firstChild.data)

def getXMLmultiple(parent='WuYA',child=None):
    xmlFile = xml.dom.minidom.parse('data.xml')
    data    = xmlFile.documentElement
    itemList = data.getElementsByTagName(parent)
    item = itemList[0]
    print(item.getAttribute(child))


print(getXMLalone('yan'))
print(getXMLmultiple('WuYA','sex'))
print(getXMLmultiple(child='sex'))
