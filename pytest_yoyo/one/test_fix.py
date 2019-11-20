# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 15:54
# @Author  : alvin
# @File    : test_fix.py
# @Software: PyCharm

import  pytest
#  里面没有参数，那么默认scope=”function”，也就是此时的级别的function，针对函数有效
@pytest.fixture()
def login():
    print("login input username && paasword")
def test_s1(login):
    print("case 1:login after do something action")
def test_s2():
    print("case2 : not login action22")
def test_s3(login):
    print("case3:login after do somethig 33")

if __name__ == "__main__":
    pytest.main(["-s","test_fix.py"])