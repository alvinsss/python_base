#author:alvin
#coding:utf8
lista = [1,2,3,"aaa",4,5,6,7]
lista.append("alvin")
print(lista)
lista.insert(2,"alvin")
print(lista)
lista.remove("alvin") #删除第1次出现的
print(lista)

ls1=[1,2,3,"this is a list1"]
ls2=[4,5,6,"这是第2个列表"]
print(ls1+ls2)
print(ls1*2)
print(ls1[0],ls1[1:3:1],ls1[2:])

str1 = "summer"
print(str1[1])
print('s' in str1)
for  i in str1:#遍历字符串和列表
    print(i)

dict1={"name":"alvin","age":19,"sex":"女"}
print(dict1)
