#author:alvin
#coding:utf8

fn  = "new.txt"
fd  = open(fn,"r+")
fr  = fd.read()
fd.write('wwwwwwwwwww')

fd.close()
