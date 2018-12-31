#author:alvin
#coding:utf8

import  re

str1 = "abc"
str2 = r'abc'
str3 = 'top tip tqp twp tep'
res = re.findall(str2,"aaaaa")
res2 = re.findall(str2,"abc")
res3 = re.findall("top",str3)
findstr = r"t[io]p"
res3 = re.findall(findstr,str3)
print( res,res2,res3)
str4 = "hello world ,hello boy"
r= r"hello"
r1= r"^hello" #hello开头
r2= r"boy$" #行尾
res4 = re.findall(r,str4)
res5 = re.findall(r1,str4)
res6 = re.findall(r2,str4)
print(res4,res5,res6)
str6= r"x[0123456789]x"
print(re.findall(str6,"x1x x2x"))


