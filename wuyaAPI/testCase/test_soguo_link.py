#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f12.py
@time: 2019/01/13
"""
import unittest
from selenium import  webdriver
import time
from python_base.wuyaAPI.day10 import fun_init

class  SoguoLink(fun_init.InitENV):
    def test_sogou_news(self):
        '''测试title'''
        self.assertEqual(self.dr.title,"搜狗搜索引擎 - 上网从搜狗开始")

    def test_sogou_kwstatus(self):
        '''测试搜索的输入框是否可以编辑'''
        so=self.dr.find_element_by_id('query')
        self.assertTrue(so.is_enabled())

# if __name__ == "__main__":
#     unittest.main(verbosity=2)
