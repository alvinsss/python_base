#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f1.py
@time: 2019/01/12
"""
import unittest
class F1(unittest.TestCase):
#先setUp 测试方法 最后tearDown
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")
    def test_001(self):
        print("test_001")
    def test_002(self):
        self.assertEqual(1,'1')


if __name__ == "__main__":
    unittest.main(verbosity=2)