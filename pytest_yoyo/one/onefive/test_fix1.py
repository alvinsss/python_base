# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 16:10
# @Author  : alvin
# @File    : test_fix1.py
# @Software: PyCharm
import pytest
def test_s1(login):
    print("case 1:login do something action11")
def test_s2():
    print("case2 : not login action22")
def test_s3(login):
    print("case3:login after do somethig 33")
if __name__ == "__main__":
    pytest.main(['-s',"test_fix1.py"])