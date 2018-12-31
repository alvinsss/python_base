#author:alvin
#coding:utf8
from functools import reduce

name =['alvin','wang','tom']
age = [20,30,40]
tel=['133','156','189']
print(str(zip(name,age,tel)))
l1 = range(1,101)
n = 0
for i in l1:
    n = i+n
    # print(n)
def rf (x,y):
    return x+y
print(reduce(rf,l1))
print( lambda  x,y:x+y,l1)
print( lambda  x:x%2 ==0,l1)

