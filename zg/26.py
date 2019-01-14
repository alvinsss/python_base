#author:alvin
#coding:utf8

import  re

# str1 = "abc"
# str2 = r'abc'
# str3 = 'top tip tqp twp tep'
# res = re.findall(str2,"aaaaa")
# res2 = re.findall(str2,"abc")
# res3 = re.findall("top",str3)
# findstr = r"t[io]p"
# res3 = re.findall(findstr,str3)
# print( res,res2,res3)
# str4 = "hello world ,hello boy"
# r= r"hello"
# r1= r"^hello" #hello开头
# r2= r"boy$" #行尾
# res4 = re.findall(r,str4)
# res5 = re.findall(r1,str4)
# res6 = re.findall(r2,str4)
# print(res4,res5,res6)
# str6= r"x[0123456789]x"
# print(re.findall(str6,"x1x x2x"))
# s= 'abc'
# print(re.findall(s,'aaaaaabca'))
# st = "top tip tqp twp tep"
# print(re.findall("top",st))
# res = "t[io]p"
# print(re.findall(res,st))
# sss= "hello world hello boby"
# r = "^hello"
# r = "boby$"
# print(re.findall(r,sss))
r1 = re.compile(r'[csvt]',re.I)
print(r1.finditer("cs"))
print(r1.match('aa csvt hello'))
x = r1.match('csvt hello')
print( x.group())

s = "hello csvt"
print(s.replace('csvt','python'))
rs = r'c..t'
print(re.sub(rs,'python','csvt caat cvvt cccc'))

ip = "1.2.3.4"
print(ip.split('.'))
s = "123+456-789*000"
print(re.split(r'[\+\-\**]',s))

rtel = r"\d{3,4}-\d{8}"
print(re.findall(rtel,"010-12345678"))

rtp = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
print(re.findall(rtp,"192.168.0.1"))
