#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: configTest.py
@time: 2019/01/15
"""
import  configparser
import  os
def base_dir(filename=None):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),'config',filename)

def getLinux(linux='linux'):
    list1=[]
    config = configparser.ConfigParser()
    config.read(base_dir('config.ini'))
    print(base_dir('config.ini'))
    ip=config.get(linux,'IP')
    port=config.get(linux,'PORT')
    username=config.get(linux,'USERNAME')
    passwd=config.get(linux,'PASSWORD')
    print(ip,port,username,passwd)
    list1.append(ip)
    list1.append(port)
    list1.append(username)
    list1.append(passwd)
    return list1



print(getLinux()[0])