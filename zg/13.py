import  time
d = {1:111,2:222,5:555,3:333}
for k,v in d.items():
    print(k,v)
else:
    print("ending")

for x in d:
    print(d[x])
else:
    print("ending")

for x in range(1,11):
    print(x)
    time.sleep(1)
    if  x == 2:
        print("x=============2")
        continue #跳出当次循环
    if x == 3:
        pass #站位
    # if x == 5:
    #     exit() #程序停止
    if  x == 6:
        break #跳出当层循环
    print('#'*50)
    if x == 7:
        pass #站位
else:
    print("ending")

for x in range(1,11):
    print("------------>",x)