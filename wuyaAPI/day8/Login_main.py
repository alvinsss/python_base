#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: Login.py
@time: 2019/01/13
"""
import  Login
def main():
    per = Login.LoginC("alvin","admin")
    while True:
        try:
            t = input('选项1、注册 2、登录 3、退出  请输入：')
            print(type(t))
                #判断输入是否浮点数据
            if isinstance(t,float):
                t = int(t)
            elif isinstance(t,str):
                if len(t) == 1:
                    t= int(t)
                else:
                    #第个字符处理成数字
                    t = int(ord(list(t)[0]))

        except Exception as e:
            print(e.args)

        else:
            if   t == 1:
                per.register()
            elif t == 2:
                per.userInfo()
            elif t == 3:
                exit()
            else:
                print("选项不存在,请重新输入！")
        finally:
            pass



if __name__ == '__main__':
    main()