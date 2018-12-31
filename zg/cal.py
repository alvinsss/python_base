
#author:alvin
#coding:utf8
# from __future__ import  division
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

if __name__ == "__main__":
    operator(2, "*", 3)