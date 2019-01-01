][]

#author:alvin
#coding:utf8
# from __future__ import  division
'''
def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y

def operator(x,o,y):
    if o == "+":
        print(jia(x,y))
    if o == "-":
        print(jian(x,y))
    if o== "*":
        print(cheng(x,y))
    if o== "/":
        print(chu(x,y))
    else:
        pass

operator(2,'+',4)
operator(2,'-',4)
operator(2,'*',4)
operator(2,'/',4)
'''
def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y

operator ={"+":jia,"-":jian,"*":cheng,"/":chu}

print(chu(3,2))
# print(operator["/"](3,2))
# print(operator.get("/")(3,2))

def f(x,o,y):
    print(operator.get(o)(x,y))

# print(f(3,"+",2))

x=1
y=2
operators="/"
result ={
    "+":x+y,
    "-":x-y,
    "*":x*y,
    "/":x/y
}
print(result.get(operators))
