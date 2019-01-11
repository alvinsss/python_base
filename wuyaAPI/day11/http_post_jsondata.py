#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f1.py
@time: 2019/01/10
"""
import  requests
import  json
data={"username":"2","password":"111"}
headers={
    'Content-type':'application/json;charset=utf-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
}
#json=使用json的
r = requests.post(url="https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
  ,json=data,headers=headers)

# r = requests.post(url="https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
#   ,data=json.dumps(data),headers=headers)
print(  json.dumps(r.json(),indent=True,ensure_ascii=False) )