#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: httpJson.py
@time: 2019/01/09#!usr/bin/env python
#-*- coding:utf-8 _*-
@author:alvin
@file: httpJson.py
@time: 2019/01/08
"""
import  json
import  requests
import sys;
print  (sys.getdefaultencoding())
# res = requests.post(
#     url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019021726322',
#     data={"phoneNumber":"18610392330","internationalAreaCode":"+86","rsaPassword":"TEDmLtu9oUnTaiCfie4"
#            "XhP7QOfsus2fhQOx16g6DZ1CtRraBOoRmiVDluIB4/sB6mQ6IDN90VIr2W1SlxmYy7SlgZlTOMcWovz6eE3axYUVHx7jR3DI1ZrMO2iniUhuZLWS1zYOTRQ9q3z49i7ZR/oDSxcpnP4NQYBWJM87Jgo=",
#           "persistenceHint":"true","publicKey":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCROXqyCKxG8DrQKvrmdwiAHFJseaLHKsdzJ+61EpEGUawyLk5obn2Z2lyVVGjqT3KECk3DJtAD6Jux/m/gW2/lxspvhUO1YE1P8OZuUq5xhr/3AWuSSXCqLM2q6TEMnI2VE1BzlsRcxQVGVd4kGszzpyLXYS9ubFTTp1C2A+uZ1QIDAQAB"}
#             ,Origin={"http://www.renren.com"}   )

# print(res.status_code)
# print(res.text)
'''
序列化：把python的数据转str的类型
反序列化:str转python的数据类型
'''
# 字典类型
# dict1={'name':'alvin','age':18}
# dic_str =json.dumps(dict1)
# print(dic_str,type(dic_str))
# str_dic = json.loads(dic_str)
# print(str_dic,type(str_dic))
#
# '''列表的序列化和反序列化'''
# list1 =['admin','alvin','qatest']
# list_str=json.dumps(list1)
# print(list_str,type(list_str))
# str_list = json.loads(list_str)
# print(str_list,type(str_list))
# '''元组的序列化和反序列化'''
# tuple1=('alvin','qatest','a',['a',1])
# tuple_str = json.dumps(tuple1)
# print(tuple_str,type(tuple_str))
# str_tuple=json.loads( tuple_str)
# print(str_tuple,type(str_tuple)) #列表

res = requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
# print(res.text.encode('utf-8'))u
#对文件的序列化->把服务端的数据写文件中
# 1,你先看下返回的r.encoding是什么编码
# 2,对这个编码进行解码
# 3,解码之后再编码成utf-8
print(res.content.decode("utf-8"),type(res.content))
fd = open('w.json','w')
fd.write(res.content.decode("utf-8"))
json.dump(res.content.decode("utf-8"),open('weather.json','w',encoding='utf-8'),ensure_ascii=True)
#文件的反序列化：读取文件的内容
# print(json.load(open('weather.json','r')))