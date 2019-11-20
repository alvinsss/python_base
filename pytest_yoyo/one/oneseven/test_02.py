# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 17:05
# @Author  : alvin
# @File    : test_02.py
# @Software: PyCharm
import  pytest

@pytest.fixture(scope="function")
def start(request):
    print("\n-------start exec function---")
@pytest.mark.usefixtures("start")
def test_a():
    print("-------case a exec -----")
@pytest.mark.usefixtures("start")
class Test_aaa():
    def test_01(self):
        print("-----case 01 ---")
    def test_02(self):
        print("-----case 02 ---")
if __name__ == "__main__":
    pytest.main(["-s","test_02.py"])