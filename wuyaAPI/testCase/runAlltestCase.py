#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: runAlltestCase.py
@time: 2019/01/14
"""
import  unittest
import  os
def getAllTestCase():
    '''获取指定文件夹下的test_*.py 文件'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return  suite

def run():
    unittest.TextTestRunner(verbosity=2).run(getAllTestCase())

if __name__ == "__main__":
    run()