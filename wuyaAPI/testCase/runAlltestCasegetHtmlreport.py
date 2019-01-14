#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: runAlltestCasegetHtmlreport.py
@time: 2019/01/14
"""
import  unittest
import  os
import  HTMLTestRunner
import  time as t
def getAlltestCase():
    getsuite=unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern="test_*.py",
        top_level_dir=None
    )
    return  getsuite

def run():

    fp = os.path.join(os.path.dirname(os.path.dirname(__file__)),'report',getnowtime()+'report.Html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp,'wb'),
        title='api自动化测试报告',
        description='详情信息'
    ).run(getAlltestCase())

def getnowtime():
    nowtime = t.strftime('%Y-%m-%d %H_%M_%S',t.localtime(t.time()))
    return  nowtime


if __name__ == "__main__":
    run()
