#author:alvin
#coding:utf8
import  re
str1 = "abcdada123456789"
str2 = "010-12345678"
fstr1 = r"\^abc"
fstr2 = r"\d"
#fstr3 = r"^010-[0-9]"
#fstr3 = r"^010-\d\d\d\d\d\d\d\d"
fstr3 = r"^010-\d{8}"
r = r"ab"
print(re.findall(str1,fstr1),re.findall(str1,fstr2))
print(re.findall(str2,fstr3))
print(re.findall(r,'abbbbbb'))
r = r"ab+"
r1 = r"ab+?"
print(re.findall(r,'abbbbbb'))
print(re.findall(r1,'abbbbbb'))

r = r"^010-?\d{8}$" #? 0或1次
print(re.findall(r,'01012345678'))
print(re.findall(r,'010-12345678'))
print(re.findall(r,'010--12345678'))

r = r"a{1,3}"
print(re.findall(r,'a'))
print(re.findall(r,'aaa'))
print(re.findall(r,'aaaa'))


