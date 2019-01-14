#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: Login.py
@time: 2019/01/13
"""
import  json
class LoginC(object):
    def __init__(self,username,passwd):
        self.username = username
        self.passwd   = passwd
    def getUsername(self):
        return  self.username
    def setUsername(self,name):
        self.username= name
    def getPasswd(self):
        return  self.passwd
    def setPasswd(self,passwd):
        self.passwd = passwd

    def login(self):
        f = str(json.load(open('login','r')))
        list1 = f.split('|')
        if list1[0] == self.username and list1[1] == self.passwd:
            return  True
        else:
            return False
    def register(self):
        temp = self.username+'|'+self.passwd
        json.dump(temp,open('login','w'))
        print("注册成功")
    def userInfo(self):
        f = str(json.load(open('login','r')))
        list1 = f.split('|')
        r = self.login()
        if r:
            print("恭喜{0}进入系统".format(list1[0]))
        else:
            print("sorry login fail")