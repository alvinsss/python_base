#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f1.py
@time: 2019/01/10
"""
import  requests

# r = requests.get(url="https://movie.douban.com/")
# r=requests.get(url="https://movie.douban.com/subject_search?search_text=alvin&cat=1002")
getdata={'search_text':'alvin','cat':1002}
r=requests.get(url="https://movie.douban.com/subject_search?",params=getdata)

print(r.status_code)
# 确定返回是html
print(r.text)
# print(r.content.decode('utf-8'))
# print(r.url,r.encoding)
#确定是json格式
# print(r.json())