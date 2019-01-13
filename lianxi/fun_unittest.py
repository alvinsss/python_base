#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: fun.py
@time: 2019/01/13
"""
import unittest
import fun
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

if __name__ =='__main__':
  unittest.main()