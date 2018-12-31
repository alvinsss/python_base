#author:alvin
#coding:utf8
import  pymysql
pymysql.install_as_MySQLdb()

def search():
    conn =  pymysql.connect(host="localhost",user="root",passwd="",db="test")
    cursor = conn.cursor()
    exec_sql = cursor.execute("SELECT * from user")
    exec_data = cursor.fetchall()
    # print(exec_data)
    cursor.close()
    conn.close()
    return  exec_data

def updata():
    conn = pymysql.connect(host="localhost",user="root",passwd="",db="test")
    cursor = conn.cursor()
    exec_sql = cursor.execute('UPDATE user set age=age+1 WHERE `name`="alvin"')
    result = conn.commit()
    cursor.close()
    conn.close()

print(search())
print(updata())