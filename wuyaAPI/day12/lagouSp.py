#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: lagouSp.py
@time: 2019/01/15
"""
import requests
import time
import csv
url='https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
def getHeader():
    headers={
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie':'JSESSIONID=ABAAABAAAIAACBIC8FB3664604EDAA48AB8BC31604D1068; user_trace_token=20190115202537-a9dc9212-18c0-11e9-b310-525400f775ce; LGUID=20190115202537-a9dc9461-18c0-11e9-b310-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=3a2b5b6c74e0407d9313fd118be0cff8; _ga=GA1.2.1734538929.1547555137; _gid=GA1.2.1993790329.1547555137; LGSID=20190115202537-a9dc92fd-18c0-11e9-b310-525400f775ce; LGRID=20190115211349-65ec407a-18c7-11e9-b33d-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547555137; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547558030',
        'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='
    }
    return headers

def laGou(page=5):
    positions=[]
    time.sleep(10)
    r = requests.post(url=url,
                      headers=getHeader(),
                      data={'first':False,
                            'pn':page,
                            'kd':"自动化测试工程师"
                            }
                      )
    # print(r.text)
    for i in range(15):
        companyFullName=r.json()['content']['positionResult']['result'][i]['companyFullName']
        district=r.json()['content']['positionResult']['result'][i]['district']
        stationname=r.json()['content']['positionResult']['result'][i]['stationname']
        education=r.json()['content']['positionResult']['result'][i]['education']
        workYear=r.json()['content']['positionResult']['result'][i]['workYear']
        positionName=r.json()['content']['positionResult']['result'][i]['positionName']
        salary=r.json()['content']['positionResult']['result'][i]['salary']
        skillLables=r.json()['content']['positionResult']['result'][i]['skillLables']

        position={
            '公司全称':companyFullName,
            '地区':district,
            '地点':stationname,
            '教育':education,
            '年限': workYear,
            '职位': positionName,
            '薪资': salary,
            '技能': skillLables,
        }
        positions.append(position)

    for item in positions:
        print(item)
    return positions


def writeCSV():

    header_csv={'公司全称','地区','地点','教育','年限','职位','薪资','技能'}
    with open('lagou.csv', 'w', newline='', encoding='gbk') as fh:
        writer_header = csv.DictWriter(fh, header_csv)
        writer_header.writeheader()

        for item in range(1, 8):
            positions=laGou(page=item)
            print(positions)
            #newline 空行   gbk操作系统国际化
            with open('lagou.csv','a',newline='',encoding='gbk') as f:
                writer_data = csv.DictWriter(f, header_csv)
                writer_data.writerows(positions)

if __name__ == "__main__":
    writeCSV()