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
@file: f6.py
@time: 2019/01/12
"""
import unittest


class F6(unittest.TestCase):
#先setUp 测试方法 最后tearDown
    def test_002(self):
        '''删除'''
        print("del")
        pass
    def test_001(self):
        '''增加'''
        print("add")
        pass

if __name__ == "__main__":
    #套件 安装测试类
    suite = unittest.TestSuite(unittest.makeSuite(F6))
    unittest.TextTestRunner.run(suite)