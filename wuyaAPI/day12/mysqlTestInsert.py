#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: mysqlTest.py
@time: 2019/01/15
"""
import  pymysql
pymysql.install_as_MySQLdb()

def connMySQLinsert():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='qa',
            passwd='qatest',
            db='test'
        )
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        #单条语句的插入
        # sql = "insert into user (age,username,password) values (%s,%s,%s)"
        # params = ('21','test1','test')
        # cur.execute(sql,params)

        #批量插入
        sql = "insert into user (age,username,password) values (%s,%s,%s)"
        params = [('21','test1','test'),('22','test2','test'),('21','test3','test')]
        cur.executemany(sql,params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

connMySQLinsert()






