# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 20:22
# @Author  : alvin
# @File    : test_01.py
# @Software: PyCharm
import  pytest
@pytest.mark.parametrize("test_input,expected",
                         [("3+5",8),
                          ("2+4",6),
                          pytest.param("6*9",42,marks=pytest.mark.xfail),
                         ])
def test_eval(test_input,expected):
    assert eval(test_input) == expected
if __name__ == "__main__":
    pytest.main(['-s',"test_01.py"])