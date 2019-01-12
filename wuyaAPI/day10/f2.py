#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f2.py
@time: 2019/01/12
"""
#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f1.py
@time: 2019/01/12
"""
import unittest
from selenium import webdriver
class F1(unittest.TestCase):
#先setUp 测试方法 最后tearDown
    @classmethod
    def setUpClass(cls):
        print("setup")
        cls.dr = webdriver.Firefox()
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(30)
        cls.dr.get("https://www.baidu.com")
    @classmethod
    def tearDownClass(cls):
        print("tearDown")
        cls.dr.quit()
    def test_baidu002Dtu(self):
        '''百度地图测试'''
        print("test_baidu002Dtu")
        self.dr.find_element_by_link_text('地图').click()
        self.dr.forward()
    def test_baidu001new(self):
        '''百度新闻测试'''
        print("test_baidu001new")
        self.dr.find_element_by_link_text('新闻1').click()
        self.dr.forward()


if __name__ == "__main__":
    unittest.main(verbosity=2)