
#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: webui.py
@time: 2019/01/13
"""
from selenium import  webdriver

def test():
    dr = webdriver.Chrome()
    dr.get("https://www.baidu.com")
    dr.maximize_window()
    print(dr.title)
    dr.close()

if __name__ == "__main__":
    test()