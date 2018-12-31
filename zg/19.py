#author:alvin
#coding:utf8
def f(x):
    print( x)

print( f(10) )
print( f('hello') )
print( f([1,2,3,4]) )
print( f({1:111,2:222,3:333,4:"444"}) )
print( f(range(10)) )
print("#"*30)

def f1(x,y):
    print(x,y)
print(f1(1,2))
t = ('a','b')
# print( f1(t) )
print( f1(t,'test'))
t = ('name','alvin')
t1 = ('name','alvin','30')

def f2(x,y):
    print("%s:%s"% (x,y))

print( f2(*t) )
# print( f2(*t1) )

def f3(name='name',age=0):
    print("name:%s" %name)
    print("age:%s" %age)
print(f3("alvin", 30))
t2=(30,'alvin')
print(f3("alvin",30))
dic1={'name':'alvin','age':30}
print(f3(name="alvin",age=30))
print(f3(**dic1))
print(f3(dic1['name'],dic1['age']))

#元组
def fd(x,*args):
    print(x)
    print(args)
print(fd(1))
print(fd(1,2,3))
#元组 字典
def fdd(x,*args,**kw):
    print(x)
    print(args)
    print(kw)
print(fdd(1,2,3,4,5,6,y=20,z=30))