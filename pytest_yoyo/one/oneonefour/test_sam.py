# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 10:36
# @Author  : alvin
# @File    : test_sam.py
# @Software: PyCharm
import pytest
def test_ans(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0
if __name__ == "__main__":
    pytest.main(["-s","test_sam.py","--cmdopt","type2"])