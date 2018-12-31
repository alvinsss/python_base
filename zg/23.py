#author:alvin
#coding:utf8
import  string
s="dass3232"
print(s.capitalize())
print(s.replace("ss","good"))
ss ="123123123"
print(ss.replace('1','X',1))
#help(str.replace)

list1 =[1,2,3,"SSS"]
print(list1.append("good"))

ip = "192.168.1.123"
print(ip.split('.'))
print(ip.split('.',2))

def f(x):
    if x > 5:
        return True
l = range(10)
print(f(6))

print(filter(f,l))



