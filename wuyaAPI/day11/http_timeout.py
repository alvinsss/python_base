#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f1.py
@time: 2019/01/10
"""
import  requests
#时间不确定 可以轮询
r = requests.get(url="https://movie.douban.com/",timeout=2)
print(r.status_code,r.text)