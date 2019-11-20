#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: fun.py
@time: 2019/01/13
"""
import unittest
from lianxi import fun
import re

class mytest(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass
  #具体的测试用例，一定要以test开头
  def testsum(self):
    self.assertEqual(fun.sum(1, 2), 3, 'test sum fail')

  def test_decode(self):
    by = b'package:com.github.uiautomator\r\r\n'
    by_r = rb'package:com.github.uiautomator\r\r\n'
    by_str = by.decode( 'utf-8' )
    byr_str = by_r.decode( 'utf-8' )
    print("by_str",by_str)
    print("by_str end ")
    print("byr_str" ,byr_str,type(byr_str) )
    print("byr_str_n" ,byr_str.strip(r'\n').replace(r'\r',''),type(byr_str) )
    print("byr_str_QP" ,byr_str[0:-6] )
    print("byr_str_nreplace" ,byr_str.replace(r'\n','').replace(r'\r',''),type(byr_str) )

if __name__ =='__main__':
  unittest.main()