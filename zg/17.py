#author:alvin
#coding:utf8

a = "global a"
def fun():
    global a
    a = 100
    global  y
    y = 200

print(a)
fun()
print("#"*30)
print(a)
