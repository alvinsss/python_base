#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: sp163.py
@time: 2019/01/12
"""
import requests
url = "https://log.study.163.com/api/v1/log.do"
data = {"product":"study","data":"tBNRNRL3voM2IMDE2ywG2XhNXpkfOl3FbJ+NAF5cz7/RnYW5/E1aHBok1GJXJBQhLqL47ZFYuxlyGU8LkVbELDHswfYq8XxjyzH172dBB1Wt1Gg8Rr/rDoxztLSA4+gyS7KQ9L8U4BHi3sWQygPYlnr15Yfi32xmF31QyPRSttaqDUAcNefEZSNfPRWZoSm6SYvKx6FeCeg6+lyC7vVLXFrDYSj173dwvoPqyCy5sBv/WA2l4R9cQGHq0ZVctViGZCv4IFxzcGT0+M/JmlZKHbauC41lCyQKQ1WqSOtjwQFdOx9zJKmvjeUEqRhoFVImjkvwTGks27nNLzC8GFxHeQPNp16gDYVDJHQyGjRZptmt4tzAopWVUioWOt9rGYzRsuq/GkCODcBIzntOCZ+JYA==","meta":{"deviceDisinctId":"51a8521174ea406188f3dc1c887b2178","screenResolution":"1600*900"}}
header={'Accept':'application/json','Accept-Language':'zh-CN,zh;q=0.9'
        ,'Content-Type':'application/json','device-id':'51a8521174ea406188f3dc1c887b2178','edu-app-type':'web'
        ,'Host':'log.study.163.com','Origin':'https://study.163.com','Referer':'https://study.163.com/'
        ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
        ,'Accept-Encoding':'gzip, deflate, br'}

res = requests.post(url=url,data=data,headers=header,verify=False)
print(res.status_code)



































# header ={'Access-Control-Allow-Credentials':'true','Access-Control-Allow-Headers':'*','Access-Control-Allow-Methods':'GET,POST,OPTIONS'
#          ,'Access-Control-Allow-Origin':'https://study.163.com','Access-Control-Expose-Header':'Set-Cookie,Max-Age'
# ,'Content-Type':'application/json;charset=UTF-8','Transfer-Encoding':'chunked','Vary':'Accept-Encoding'}