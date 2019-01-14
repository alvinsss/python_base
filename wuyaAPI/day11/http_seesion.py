#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: http_seesion.py
@time: 2019/01/14
"""
'''会话对象:Session'''
import  requests
def getHeader():
		headers={
			'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Content-Type':'application/x-www-form-urlencoded'}
		return headers

data={
	     'email':'13221454225',
	     'icode':'',
	     'origURL':'http://www.renren.com/home',
	     'domain':'renren.com',
	     'key_id':1,
	     'captcha_type':'web_login',
	     'password':'31a7f0da50cdb967b72610ca996e30fb2f64d2c93dc40283688e9491077e6ae6',
	     'rkey':'5aa2d6b85ce9f85402f2fa3af466d326',
	     'f':'https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_r-h4h4RsVJtWYvcrgiTSe0'}

def login():
	#对Session类进行实例化
	s=requests.Session()
	r=s.post(
		url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019011947419',
		data=data,
		headers=getHeader())
	return s

def getProfile():
	r=login().get('http://www.renren.com/969444156/profile')
	print(r.text)

getProfile()

