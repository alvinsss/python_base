#author:alvin
#coding:utf8
import  re
import  os
# fn = "new.txt"
# fd = open(fn)
# s1 =  fd.read()
# print(s1)
# fd.close()
#
# for i in open(fn):
#     print(i)
#
# fn = "new.txt"
# fd = open(fn)
# s1 =  fd.readline()
# print(s1)
# fd.close()
#
# fn = "new.txt"
# fd = open(fn)
# s2 =  fd.readlines()
# print(s2)
# fd.close()
#
#
# fn = "new.txt"
# list1 = ['one\n','two\n','three\n']
# fd = open(fn,'a')
# fd.write("\n")
# fd.writelines(list1)
# fd.close()
#
# fn = "new.txt"
# list1 = ['one\n','two\n','three\n']
# fd = open(fn,'w')
# fd.writelines(list1)
# fd.flush()
# fd.close()
#一行查找一次
fn = "new.txt"
fd = open(fn,"r")
count = 0
for s in fd.readlines():
    li = re.findall("hello",s)
    if len(li)>0:
        # print(s,li)
        count = count +len(li)
print(count)

#字符串查找 返回list
# fn = "new.txt"
# fd = open(fn,"r+")
# r  = fd.read()
# retarget = "hello"
# # print(re.findall(retarget,r))
# print(len(re.findall(retarget,r)))
# repstr = r.replace(retarget,"csvt")
# print(repstr)
# fw = "new2.txt"
# fdw = open(fw,"w+")
# fdw.write(repstr)
# fdw.close()
# # wfile = fd.write(repstr)
# fd.close()
# os.remove(fn)
# os.rename(fw,fn);#重命名
#

# fd1=open("f1.txt","r")
# fd2=open("f2.txt","w+")
# for s in fd1.readlines():
#     fd2.write(s.replace("hello","csvt"))
# fd1.close()
# fd2.close()

fpseek = open("seek.txt","r+")
s = fpseek.read()
print(s)
fpseek.seek(0,0)
rs =s.replace("hello","csvt")
print(rs)
fpseek.write(rs)
fpseek.close()

#遍历文件每个字符
# fn = "new.txt"
# fr = open(fn,"r")
# r  = fr.read()
# target = "t"
# count = 0
# for index,value in enumerate(r):
#     # print(value) 字符串一个一个输出
#     if target == value:
#         print(target,'出现位置',index)
#         count = count +1
# print(target,"出现次数",count)
# fr.close()

