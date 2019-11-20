# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 15:57
# @Author  : alvin
# @File    : date_de.py
# @Software: PyCharm
import  datetime
import  copy

# 默认每月的1号开始
def get_current_date_start(date_num='01'):
    date_start_list = []
    get_current_date_list = (str(datetime.date.today())).split('-')
    get_current_date_last = (str(datetime.date.today())).split('-')[2]
    if int(get_current_date_last) <= int( date_num ):
        return (str( datetime.date.today() ))
    else:
        date_start_list = copy.deepcopy( (str(datetime.date.today())).split('-'))
        date_start_list.pop()
        date_start_list.append( date_num )
        get_current_date = str(datetime.date.today()).split( '-' )
        return '-'.join( date_start_list )


if __name__ == "__main__":
    print( get_current_date_start( '30' ) )
