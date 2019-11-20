# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 21:18
# @Author  : alvin
# @File    : test_01mark.py
# @Software: PyCharm
import pytest
@pytest.mark.httpweb
def test_httpweb():
    print("httpweb")
def test_ui_ios():
    print("ios ui test")
class TestClass:
    def test_method(self):
        pass
if __name__ == "__main__":
    pytest.main(["-s","test_01mark.py","-m='not httpweb'"])