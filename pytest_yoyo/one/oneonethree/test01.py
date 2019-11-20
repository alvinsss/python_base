# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 22:10
# @Author  : alvin
# @File    : test01.py
# @Software: PyCharm
import pytest
login_data=[("admin","111111"),("admin","")]
def login(user,psw):
    print("登录的账户：%s,登录密码：%s"%(user,psw))
    if psw:
        return True
    else:
        return False
@pytest.mark.parametrize("user,psw",login_data)
def test_login(user,psw):
    result = login(user,psw)
    assert result == True

if __name__ == "__main__":
    pytest.main(["-s","test01.py"])