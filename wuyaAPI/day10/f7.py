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
@file: f7.py
@time: 2019/01/12
"""
import unittest



class F7(unittest.TestCase):
    def setUp(self):
        print("F7 setup")
#先setUp 测试方法 最后tearDown
    def test_002(self):
        '''删除'''
        print("F7 del")
        pass
    def test_001(self):
        '''增加'''
        print("F7 add")
        pass
    def tearDown(self):
        print("F7 tearDown")

class F8(unittest.TestCase):
    def setUp(self):
        print("F8 setup")
#先setUp 测试方法 最后tearDown
    def test_002(self):
        '''删除'''
        print("F8 del")
        pass
    def test_001(self):
        '''增加'''
        print("F8 add")
        pass
    def tearDown(self):
        print(" F8 tearDown")
if __name__ == "__main__":
    #套件 按照类文件执行
    suite = unittest.TestLoader().loadTestsFromModule('f7.py')
    unittest.TextTestRunner(verbosity=2).run(suite)