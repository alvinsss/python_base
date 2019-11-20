# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 16:31
# @Author  : alvin
# @File    : test_f1.py
# @Software: PyCharm
import pytest
@pytest.fixture(scope="module")
def open():
    print("open explor baidu page")
    yield
    print("exec treardown!")
    print("close explor")
def test_s1(open):
    print("case1:search python-1")
def test_s2(open):
    print("case2:search python-2")
def test_s3(open):
    print("case3:search python-3")
if __name__ == "__main__":
    pytest.main(['-s',"test_f1.py"])