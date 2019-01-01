#author:alvin
#coding:utf8
import errno
filename = input("please input:")
try:
    fOpenFile =open(filename)
    print(xxx)
except IOError:
    print("io error")
    pass

except NameError:
    print("name error")
    pass
finally:
    print("ok")

if filename == "hello":
    raise KeyError("nothing")
