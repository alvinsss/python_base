#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: init.py
@time: 2019/01/12
"""
import  unittest
from   selenium import  webdriver

class InitENV (unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(3)
        self.dr.get("https://www.sogou.com")
        print("setUp")
    def tearDown(self):
        self.dr.quit()


