# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 21:44
# @Author  : alvin
# @File    : test_01xfail.py
# @Software: PyCharm
import pytest
canshu=[{"user":"admin","psw":""}]
@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw  = request.param["psw"]
    print("login info,账户:%s,密码:%s" %(user,psw))
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("login",canshu,indirect=True)
class Test_xx():
    def test_01(self,login):
        result = login
        print("case1:%s"%result)
        assert result == True
    def test_02(self,login):
        result = login
        print("case2:%s"%result)
        if not result:
            pytest.xfail("login fail,mark xfail")
        assert 1 == 1
    def test_03(self,login):
        result = login
        print("case3:%s"%result)
        if not result:
            pytest.xfail("login fail,mark xfail")
        assert 1 == 1
if __name__ == "__main__":
    pytest.main(["-s","test_01xfail.py"])