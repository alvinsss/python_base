l1=["name",'age','gender']
l2=["alvin",'30','male']
print(zip(l1,l2))
dic1 = {'name':'alvin','age':25,'gender':'male'}
print( dic1['name'])
name = 'dname'
dic2 ={1:'123',name:'alvin','x':456}
print( dic2)
dict3={"addr":"beijing","tel":1234567890}
print(dict3)
dict3['tel']=15811112222 #修改值
print("dic2",dic2)
del(dic1['age'])
dic2.pop('x') #删键值
di_s = str(dic1)
print(di_s)
dic2.clear()
print(dic2)
del(dic2) #删除dic
print(dic1.keys())
print('gender' in dic1)

