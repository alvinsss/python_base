# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 16:11
# @Author  : alvin
# @File    : conftest.py
# @Software: PyCharm

import pytest

@pytest.fixture()
def login():
    print("input username and passwd")
