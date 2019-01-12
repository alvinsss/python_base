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
import fun_init

class F8(fun_init.InitENV):

#先setUp 测试方法 最后tearDown
    def test_002(self):
        '''删除'''
        print("F7 del")
        pass
    def test_001(self):
        '''增加'''
        print("F7 add")
        pass

    @staticmethod
    def suite():
        suite = unittest.TestSuite(unittest.makeSuite(F8))
        return suite

if __name__ == "__main__":
    #套件 分离测试套件
    unittest.TextTestRunner().run(F8.suite())