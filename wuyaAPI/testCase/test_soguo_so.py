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
import sys
import  os
pdirname = os.path.dirname(os.path.dirname(__file__))
tmpdirname = os.path.join(pdirname,'day10')
sys.path.append(tmpdirname)
import fun_init

class  SoguoLink(fun_init.InitENV):
    def  test_sogou_title(self):
        '''测试浏览器的title是否包含 “搜狗” 文字'''
        self.assertIn('搜狗',self.dr.title)

    def test_sogou_inputSotext(self):
        '''测试输入的搜索内容是否与页面一致'''
        so=self.dr.find_element_by_id('query')
        so.send_keys("webdirver")
        self.dr.find_element_by_id('stb').click()
        print(so.get_attribute('value'))
        self.assertEqual(so.get_attribute('value'),'webdirver')

# if __name__ == "__main__":
#     unittest.main(verbosity=2)
