#author:alvin
#coding:utf8
import  copy
listR=[1,2,3,'b','a','c']
listB = listR
print(listR,listB)
print(id(listR),id(listB))
listR.append('d')
print(listR,listB)

a=[1,2,3,['b','a','c']]
b=a
c=copy.copy(a)
print(id(a),id(b),id(c))
a.append('d')
print(id(a),id(b),id(c))
print(a,b,c)
print(id(a[0]),id(b[0]),id(c[0]))
print(id(a[3]),id(b[3]),id(c[3]))
a[3].append('d')
print(a,b,c)

d = copy.deepcopy(a)
print(a,b,c,d)
print(id(a[3]),id(b[3]),id(c[3]),id(d[3]))
a.append('e')
a[3].append('x')
print(a,d)
