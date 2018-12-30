x = ""

while x != "q":
    print( "hello")
    x = input("please input something. q for quit:")
    if not x:
        break #回车退出
    if x == "c":
        continue
    print("one more time~")
else:
    print("ending")