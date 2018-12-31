#author:alvin
#coding:utf8

fn = "format.txt"
fr = open(fn,"r")
#r  = fr.readline()
r  = fr.readlines()
print(type(r))
r[0].split("\n")
print(r[0])
fr.close()
