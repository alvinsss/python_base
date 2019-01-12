#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: init.py
@time: 2019/01/12
"""
import  unittest
from selenium import  webdriver
class InitENV (unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.maximize_window()
        self.dr.implicitly_wait()
        self.dr.get("https://www.baidu.com")

    def tearDown(self):
        self.dr.quit()
