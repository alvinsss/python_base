# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 20:52
# @Author  : alvin
# @File    : test_01skip.py
# @Software: PyCharm
import sys
import pytest
@pytest.mark.skipif(sys.version_info < (
        3,7),reason="requires py37")
def test_function():
    print(sys.version_info)
if __name__ == "__main__":
    pytest.main(["-s","test_01skip.py"])