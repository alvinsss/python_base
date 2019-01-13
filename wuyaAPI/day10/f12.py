#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f12.py
@time: 2019/01/13
"""
import unittest
import fun_init
from selenium import  webdriver
import time

class  SoguoLink(fun_init.InitENV):
    # def test_sogou_news(self):
    #     # acc_title = "百度一下，你就知道"
    #     #         # dr_titile = self.dr.title
    #     self.assertEqual(self.dr.title,"百度一下，你就知道")

    # def test_sogou_kwstatus(self):
    #     so=self.dr.find_element_by_id('query')
    #     self.assertFalse(so.is_enabled())

    def  test_sogou_title(self):
        self.assertIn('搜狗',self.dr.title)

if __name__ == "__main__":
    unittest.main(verbosity=2)
