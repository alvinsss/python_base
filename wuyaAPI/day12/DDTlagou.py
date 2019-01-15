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
import unittest
import ddt
url='https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
def getHeader():
    headers={
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie':'JSESSIONID=ABAAABAAAIAACBIC8FB3664604EDAA48AB8BC31604D1068; user_trace_token=20190115202537-a9dc9212-18c0-11e9-b310-525400f775ce; LGUID=20190115202537-a9dc9461-18c0-11e9-b310-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F5426367.html; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=3697c26520374c3583cfde00d9031423; LGSID=20190115220858-19ec7382-18cf-11e9-b66e-5254005c3644; LGRID=20190115222850-e06e0c40-18d1-11e9-b66e-5254005c3644; _ga=GA1.2.1734538929.1547555137; _gid=GA1.2.1993790329.1547555137; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547555137; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547562530',
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
    #每页15条数据，接口从0开始
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
# @ddt.ddt
class LaGou(unittest.TestCase):

    @ddt.data((1,),(2,))
    @ddt.unpack
    def test_lg(self,page=2):
        positions_list=[]
        r= requests.post(
            url=url,
            headers=getHeader(),
            data={'first': False,
                  'pn': page,
                  'kd': "自动化测试工程师"
                  }
        )
        print(r.json()['success'])
        print(r.json()['content']['positionResult']['result'][0]['salary'])
        self.assertEqual(r.json()['success'],True)



if __name__ == "__main__":
    unittest.main(verbosity=2)