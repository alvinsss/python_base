# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 17:13
# @Author  : alvin
# @File    : test_03.py
# @Software: PyCharm
import pytest

@pytest.fixture(scope="module",autouse=True)
def start(request):
    print("\n---start exec moule---")
    print('module :%s' % request.module.__name__)
    print("------ start up explor-----")
    yield
    print("--------end test--------")
@pytest.fixture(scope="function",autouse=True)
def open_home(request):
    print("function:%s\n --- open_home--" % request.function.__name__)
def test_01():
    print("----case 01 ---")
def test_02():
    print("----case 02 ---")
if __name__ == "__main__":
    pytest.main(["-s","test_03.py"])