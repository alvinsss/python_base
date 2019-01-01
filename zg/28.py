#author:alvin
#coding:utf8
import re

r1 = r"^010-\d{8}"
print( re.findall(r1,"010-12345678") )
p_tel=re.compile(r1)
# print(type(p_tel))
print( p_tel.findall("010-12345678"))
p_csvt = re.compile(r'csvt',re.I) #匹配大小写
print( p_csvt.findall("CSvt"))
print(p_csvt.match('csvt hello'))#返回对象
print(p_csvt.match('hello csvt'))#返回None
print(p_csvt.search(' hello csvt 3dsdds'))#返回对象

p_csvt2= re.compile(r'[Cc][Ss][Vv][Tt]')
print( p_csvt2.findall("CSvt"))

print( p_csvt.findall("CSvt hello csvt csvt"))
print( p_csvt.finditer("CSvt hello csvt csvt"))
x= p_csvt.finditer("CSvt hello csvt csvt")
y=p_csvt.match('csvt csvt  hello')
print( y.group())
s = "hello csvt"
print(s.replace('csvt','python'))
rs = r'c..t'
print(re.sub(rs,'python','csvt caat cvvt cccc'))
ip = "1.2.3.4"
print(ip.split('.'))
s = "123+34*323\95"
print(re.split(r'[\+\-\*\\]',s))

