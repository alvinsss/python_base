#author:alvin
#coding:utf8
fn = "log"
fo = open(fn,"w+") #w不存的话，创建文件
w  = fo.write("123abc")
fo.close()