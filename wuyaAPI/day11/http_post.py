#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: f1.py
@time: 2019/01/10
"""
import  requests
import  json
data={'first':'false','pn':2,'kd':'自动化测试工程师'}
headers={
    'Content-type':'application/json;charset=utf-8',
    'Cookie':'JSESSIONID=ABAAABAAADEAAFI971A531B3F5F55452F68510A5DDBAB27; _ga=GA1.2.393730512.1547132646; _gat=1; user_trace_token=20190110230407-fa67595b-14e8-11e9-b2f2-5254005c3644; LGSID=20190110230407-fa675a9f-14e8-11e9-b2f2-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190110230407-fa675cfb-14e8-11e9-b2f2-5254005c3644; _gid=GA1.2.815319007.1547132646; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547132646; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=c08640f49826fb19387249607f094712; SEARCH_ID=035d51bddcfb45a088c45d3bdd4aeb52; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547132740; LGRID=20190110230543-3360a097-14e9-11e9-961d-525400f775ce',
    'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
}

r = requests.post(url="https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
  ,data=data,headers=headers)
print(  json.dumps(r.json(),indent=True,ensure_ascii=False) )