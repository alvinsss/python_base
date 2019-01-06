#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: base_dict.py
@time: 2019/01/06
"""
'''1.13字典的讲解'''
''''clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
      pop', 'popitem', 'setdefault', 'update', 'values'
'''
dict1 = {'name':'alvin','age':18,'address':'beijing'}
# print(dir(dict1))
'''获取所有的keys values'''
# print(dict1.keys())
# for key in dict1.keys():
#     print(key)
# for v in dict1.values():
#     print(v)
'''对字典的循环'''
for key,values in dict1.items():
    print(key,values)
'''获取字典的key对应的具体value值'''
# print(dict1.get('age'))
# print(dict1['age'])
# print(dir(dict1))
#pop删除指定的key对应的值并打印
# print(dict1.pop('age'))
# print(dict1)

'''判断key是否存在'''
myage = 30
if 'age' in dict1:
    if myage > dict1.get('age'):
        print("dict1.age 小于30，dict1.age is:",dict1['age'])
else:
    print("sorry no age this key")
#clear全部清空
# print(dict1.clear())
# print(dict1)
#copy 复制
dict2 = dict1.copy()
print(dict2)

'''字符串和列表之间的转换'''
str1 = 'ADMINalvinadmin'
'''str - list'''
list1=str1.split('alvin')
print( list1)
'''list - str'''
print(','.join(list1))

'''列表和元组之间的转换,---强转'''
list1=[1,2,3,4,5]
''''list -> tuple'''
tuple1 = tuple(list1)
print(tuple1)
''''tuple->list'''
list2 = list(tuple1)
print(list2)

'''字典与列表之间的转换'''
'''dict-list'''
dict2=dict1.copy()
list3 = dict2.items()
print(list3,type(list3))
'''list -> dict'''
dict2 = dict(enumerate(list3))
print(dict2,type(dict2))

#https://www.apiopen.top/weatherApi?city=%E5%8C%97%E4%BA%AC
dicweather={"code":200,"msg":"成功!","data":{"yesterday":{"date":"5日星期六","high":"高温 0℃","fx":
    "北风","low":"低温 -8℃","fl":"\u003c![CDATA[\u003c3级]]\u003e","type":"多云"},"city":"北京","aqi":"无",
                                           "forecast":[{"date":"6日星期天","high":"高温 3℃","fengli":"\u003c![CDATA[\u003c3级]]\u003e","low":"低温 -7℃","fengxiang":"西南风","type":"晴"},{"date":"7日星期一","high":"高温 2℃","fengli":"\u003c![CDATA[3-4级]]\u003e","low":"低温 -7℃","fengxiang":"北风","type":"多云"},{"date":"8日星期二","high":"高温 1℃","fengli":"\u003c![CDATA[3-4级]]\u003e","low":"低温 -8℃","fengxiang":"北风","type":"晴"},{"date":"9日星期三","high":"高温 2℃","fengli":"\u003c![CDATA[3-4级]]\u003e","low":"低温 -7℃","fengxiang":"西南风","type":"多云"},{"date":"10日星期四","high":"高温 3℃","fengli":"\u003c![CDATA[\u003c3级]]\u003e","low":"低温 -6℃","fengxiang":"西南风","type":"晴"}],"ganmao":"各项气象条件适宜，无明显降温过程，发生感冒机率较低。","wendu":"-7"}}
# print(dicweather)
"""
数据：机遇json的字符串类型的数据
1、业务状态码code 200
2、消息msg
3、数据 data
断言：
1、业务状态码：dicweather['code']
2、数据dicweather['data']['forecast'][0]['high']
3、HTTP协议状态码断言
"""
if dicweather['code'] == 200:
    print("数据dicweather:",dicweather['data']['forecast'][0]['high'])
else:
    print("get dicweather api is fail! ")
