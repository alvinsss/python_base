#author:alvin
#coding:utf8
from functools import reduce

def f1(x,y):
    return x*y

print(f1(3,2))

g = lambda  x,y:x*y
print(g(4,3))

l = range(1,6)
def f(x,y):
    return  x*y
print(reduce(f,l))