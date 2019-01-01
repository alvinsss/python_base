#author:alvin
#coding:utf8
#函数与引用
import  time

def sumTotal(x,y):
    sum = 0
    list1 = range(x,y+1)
    for i in list1:
        sum = sum +i
    return sum
