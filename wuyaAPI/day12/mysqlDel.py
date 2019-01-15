#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: mysqlTest.py
@time: 2019/01/15
"""
import  pymysql
pymysql.install_as_MySQLdb()

def connMySQL():
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
        #删除
        sql="delete from user WHERE id = %s"
        params=(9,)
        cur.execute(sql,params)

    finally:
        cur.close()
        conn.close()

connMySQL()


#元组转字典
# tuplex = ((2, "w"),(3, "r"))
# dis=dict((y, x) for x, y in tuplex)
# print(dis)



