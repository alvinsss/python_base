# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 17:00
# @Author  : alvin
# @File    : test_01.py
# @Software: PyCharm
import  time
import pytest
@pytest.fixture(scope="function")
def start(request):
    print("\n------start exec funtion----")
def test_a(start):
    print("-----case a exec-------")
class Test_aa():
    def test_01(self,start):
        print("------case 01 ------")
    def test_02(self,start):
        print("------case 02 ------")
if __name__ == "__main__":
    pytest.main(['-s','test_01.py'])