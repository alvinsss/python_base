#author:alvin
#coding:utf8
fn = "format.txt"
fd = open(fn,"w")
fd.write("%10s\t %3s\n"%("name","age"))
fd.write("%10s\t %3s\n"%("alvin","100"))
fd.close()