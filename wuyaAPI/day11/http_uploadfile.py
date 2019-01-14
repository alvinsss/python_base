#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: http_uploadfile.py
@time: 2019/01/14
"""
'''({"uploadid":"profile_publisher_photo_1547466006222","code":503,"msg":"缺少参数或参数错误, 未找到图片url","files":[]});</script>
headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryyguhYqqY1ty3ffdD'把 boundary=----WebKitFormBoundaryyguhYqqY1ty3ffdD
去掉
'''
import requests
import  re
data={
    'upload':'提交',
    '_channel':'renren',
    'privacyParams':'{"sourceControl": 99}',
    'hostid':'969444156',
    'requestToken': '606747747',
    '_rtk': 'efeb3abd'
}

files = {"file":
	        ("rrw.jpg", open("F:/rrw.jpg", "rb"), "image/jpeg",{})}

headers={'Content-Type':'multipart/form-data;',
         'Cookie':'anonymid=jqmd7hwt-kjwst; _r01_=1; l4pager=0; __utma=151146938.982227639.1547135609.1547135609.1547173000.2; __utmz=151146938.1547173000.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; depovince=BJ; jebecookies=022ad137-de79-41ec-a91a-cb6ab7e2cd31|||||; ick_login=9bcb1cc0-e902-4aba-a0bd-1b01bec4bfa7; _de=38416124616CD567AE794CB9CCA086D2; p=817237e71a66984195237e318836d4106; first_login_flag=1; ln_uact=13221454225; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=3c2b5e55170123c25a44bac65dab6b1c6; societyguester=3c2b5e55170123c25a44bac65dab6b1c6; id=969444156; xnsid=b3ebfde5; ver=7.0; loginfrom=null; jebe_key=b0b3b542-bd7b-4929-9646-29c1b71a5cdd%7C35d55e33dfeb7465177d7efa0d2b4880%7C1547464611166%7C1%7C1547464612449; wp_fold=0; XNESSESSIONID=4b8056f983f8; wp=0',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400',
         }

r_upload = requests.post(
    url='http://upload.renren.com/upload.fcgi?pagetype=addpublishersingle&hostid=969444156&callback=window.parent.handlePhotoData&uploadid=profile_publisher_photo_1547466006222',
    data=data,
    headers=headers,
    files=files
)

print(r_upload.status_code)
# print(r_upload.text)
re_data = r_upload.text
print(re_data)
tmp_data = re_data[65:]
get_data = tmp_data[:-11:1]
print(get_data)

# headers_s={'Content-Type':'application/x-www-form-urlencoded',
#          'Cookie':'anonymid=jqmd7hwt-kjwst; _r01_=1; l4pager=0; __utma=151146938.982227639.1547135609.1547135609.1547173000.2; __utmz=151146938.1547173000.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; depovince=BJ; jebecookies=022ad137-de79-41ec-a91a-cb6ab7e2cd31|||||; ick_login=9bcb1cc0-e902-4aba-a0bd-1b01bec4bfa7; _de=38416124616CD567AE794CB9CCA086D2; p=817237e71a66984195237e318836d4106; first_login_flag=1; ln_uact=13221454225; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=3c2b5e55170123c25a44bac65dab6b1c6; societyguester=3c2b5e55170123c25a44bac65dab6b1c6; id=969444156; xnsid=b3ebfde5; ver=7.0; loginfrom=null; jebe_key=b0b3b542-bd7b-4929-9646-29c1b71a5cdd%7C35d55e33dfeb7465177d7efa0d2b4880%7C1547464611166%7C1%7C1547464612449; wp_fold=0; XNESSESSIONID=4b8056f983f8; wp=0',
#          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400',
#          'X-Requested-With':'XMLHttpRequest',
#         }
# data_s="photos=%5B%7B%22code%22%3A0%2C%22msg%22%3A%22%22%2C%22filename%22%3A%22%26%2324494%3B%26%2320449%3B%26%2322270%3B%26%2329255%3B_20190112132337.jpg%22%2C%22filesize%22%3A145561%2C%22width%22%3A1080%2C%22height%22%3A1920%2C%22exifs%22%3A%5B%7B%22ExifImageLength%22%3A%221920%22%7D%2C%7B%22ExifImageWidth%22%3A%221080%22%7D%2C%7B%22Orientation%22%3A%221%22%7D%5D%2C%22images%22%3A%5B%7B%22url%22%3A%22fmn093%2F20190114%2F2050%2Flarge_3Afb_e9cf00003bdc1e83.jpg%22%2C%22type%22%3A%22large%22%2C%22width%22%3A720%2C%22height%22%3A1280%7D%2C%7B%22url%22%3A%22fmn093%2F20190114%2F2050%2Fmain_3Afb_e9cf00003bdc1e83.jpg%22%2C%22type%22%3A%22main%22%2C%22width%22%3A200%2C%22height%22%3A355%7D%2C%7B%22url%22%3A%22fmn093%2F20190114%2F2050%2Ftiny_3Afb_e9cf00003bdc1e83.jpg%22%2C%22type%22%3A%22tiny%22%2C%22width%22%3A50%2C%22height%22%3A50%7D%2C%7B%22url%22%3A%22fmn093%2F20190114%2F2050%2Fhead_3Afb_e9cf00003bdc1e83.jpg%22%2C%22type%22%3A%22head%22%2C%22width%22%3A100%2C%22height%22%3A177%7D%2C%7B%22url%22%3A%22fmn093%2F20190114%2F2050%2Fxlarge_3Afb_e9cf00003bdc1e83.jpg%22%2C%22type%22%3A%22xlarge%22%2C%22width%22%3A1024%2C%22height%22%3A1820%7D%5D%7D%5D&flag=0&album.id=1206761212&sendFeed=0&requestToken=606747747&_rtk=efeb3abd"
# r_save= requests.post(
#     url='http://upload.renren.com/facade/common/upload/969444156/photo/save',
#     headers=headers_s,
#     data=data_s
# )
# print(r_save.status_code)
# print(r_save.text)