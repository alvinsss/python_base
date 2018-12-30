# #取元素遍历
# for x in "hello":
#     print(x)

str1 = "hello"
list1 =[1,2,3,'a','b','c']
t1 = (7,8,9,'x','y')
d1 = {1:111,2:222,5:555,3:33}
i = len(str1)
for x in range(i):
    print (str1[x])

for x in list1:
    print( x)

for x in d1:
    print(x)
    print(d1[x])
    print((d1.items()))

for k,v in d1.items():
    print(k)
    print(v)