# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 16:21
# @Author  : alvin
# @File    : test_fix2.py
# @Software: PyCharm
import pytest

def test_s4():
    print("case4:login after do11")
def test_s5():
    print("case5:not login ")
if __name__ == "__main__":
    pytest.main(['-s',"test_fix2.py"])