#author:alvin
#coding:utf8
#函数与引用
import  time
import  nmb.huahua.vAuto03fun
def ergui():
    print("ergui def")

ergui()

def getHttpRes(url,req): #函数名
    print(url+"--http req!"+req) #函数体

getHttpRes("alvin","18")
#有传参 有返回值
def add(a,b):
    c = a+b
    return c

result=add(3,4)
print(result)

def strTolist(str1):
    return list(str1)
#默认参数
def strTolistget(str1="python"):
    list = []
    for i in str1:
        list.append(i)
    return list

print(strTolist("al vin"))
print(strTolistget("al vin"))
print(strTolistget())

#有传参,多参数,默认值一定后面
#def add(a=9,b):

#a 叫位置参数，b默认参数
def add(a,b=7):
    c = a+b
    print(c)
add(4)
add(4,6)

def addTotal(a,b):
    num = 0
    list1 = range(a,b+1)
    for i in list1:
        num = i+num
    return  num

start = time.time()
print(addTotal(1,9990000))
end = time.time()
print("本地调用:"+str(end-start))


start = time.time()
print(nmb.huahua.vAuto03fun.sumTotal(1,9990000))
end = time.time()
print("调用时间："+str(end-start))