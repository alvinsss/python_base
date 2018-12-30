#coding:utf8
def fun (x):
    print(type(x))
    print( x)

s = input("please input something:")
fun(s)


def fun1 (x,y):
    if x == y:
        print ("x=y")
    else:
        print("x!=y")
x = input("please input x:")
y = input("please input y:")
fun1(x,y)

def mashine(x=3,y='香蕉'):
    print("生成一个",x,"元",y,"口味的水果冰激凌")
def mashine3(y,x=5):
    print("生成一个",x,"元",y,"口味的水果冰激凌###")

# mashine(5,'巧克力')

mashine(x,y)
mashine(y='巧克力')
mashine3('巧克力')