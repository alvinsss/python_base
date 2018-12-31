#author:alvin
#coding:utf8

def add(x,y):
    print("welcome")
    return  x+y

z = add(3,2)
print(z)

def f(x,y):
    if x<y:
        return -1
    print("x<y")

print(f(1,4))
print(f(4,1))