if 1-1:
    print( "ok")
print( "main ok")

def fun():
    return  0

if fun():
    print ("if True")
else:
    print("bad")

x = int(input("please input x:"))
y = int(input("please input y:"))
if x >= 90:
    print( "a")
    if y >= 90:
        print("a")
    print("x >= 90")
elif x >= 80 :
    print("b")
elif x >= 70:
    print("c")
else:
    print("bad")
# 逻辑与
if x >= 90 and y >=90:
    print("a")
elif x >= 80 :
    print("b")
elif x >= 70:
    print("c")
else:
    print("bad")