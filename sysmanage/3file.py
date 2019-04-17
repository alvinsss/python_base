#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: 3file.py
@time: 2019/04/17
"""

def tryfile():
	try:
		f  = open('filetry1.txt','w')
		f.write("quick line here\n")
	finally:
		f.close()

def file1():
	file1 = open('file1.txt','w')
	file1.write("This is\n Some\n Random\n OutPut Text\n")
	file1.close()

def withfile():
	with open("pywith.txt","w") as f:
		f.write("this is a writeable file\n")

def readfile1():
	f = open("file1.txt","r")
	f

def main():
	# file1()

	# withfile()

if __name__ == "__main__":
	main()