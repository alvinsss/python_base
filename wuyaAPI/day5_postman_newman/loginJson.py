#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:alvin
@file: def03.py
@time: 2019/01/07
"""
'''全局和局部变量'''
'''
通过global 可以进行全局变量修改
1、模拟登录
2、登录成功之后显示成功的账户
3、模拟注册
'''
import json


def getUsername():
    username = input("please input username:\n")
    return username


def getPasswd():
    passwd = input("please input password:\n")
    return passwd


def reg(username, passwd):
    temp = username + '|' + passwd
    # fd = open('login','w')
    # fd.write(temp)
    json.dump(temp, open('logindata', 'w'))


def login(username, passwd):
    loginData = str(json.load(open('logindata', 'r')))
    list1 = loginData.split('|')
    if list1[0] == username and list1[1] == passwd:
        return True
    else:
        return False


def info(username, passwd):
    # fd = open('login','r')
    # for line in fd:
    # fd = open('logindata', 'r')
    loginData = str(json.load(open('logindata', 'r')))
    list2 = loginData.split('|')
    loginRes = login(username, passwd)
    if loginRes:
        print("恭喜", (list2[0]), " 进入系统")
    else:
        print("login fail")


def exit():
    import sys
    sys.exit(1)


def main():
    while True:
        try:
            t = int(input('选项1、注册 2、登录 3、退出  请输入：'))
        except Exception as e:
            print(e.args)
        else:
            if t == 1:
                username = getUsername()
                passwd = getPasswd()
                reg(username, passwd)
            elif t == 2:
                username = getUsername()
                passwd = getPasswd()
                login(username, passwd)
                info(username, passwd)
            elif t == 3:
                exit()
            else:
                print("选项不存在,请重新输入！")
        finally:
            pass



if __name__ == '__main__':
    main()

# name = 'alvin'
# def f1():
#     global name
#     name = 'hailin'
#     print( name)
# f1()
# f = json.dump("alvin",open('logindata','w'))
# f1 = json.load(open('logindata','r'))
# print(f,type(f))
