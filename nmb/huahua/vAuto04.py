#author:alvin
#coding:utf8
#函数与引用
import  time
# def  redPackage (amount= input("please input amount:")):
#     try:
#         if float(amount) >= 0.01 and float(amount) <=200:
#             print(amount,"已经发出！")
#         else:
#            redPackage(amount=input("please input amount(0.01~200) invalid:"))
#     except Exception as E:
#         redPackage(amount=input("please input amount invalid:"))
#
# redPackage()
# except TabError as e:
#     print(e)

def add(a,b):
    c = a+b
    return c

add(7,8)

fd = open("io.txt",'r+')
read = fd.read()
print(read)
print(fd.tell())
# fd.seek(5,0)
read5 = fd.read()
print(read5)
fd.close()

def fileToList(path):
    fd2 = open(path,'r+')
    read2 = fd2.readlines()
    fd2.close()
    return  read2
print(fileToList('io.txt'))



