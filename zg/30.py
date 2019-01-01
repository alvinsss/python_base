#author:alvin
#coding:utf8
import  re
import  os
import time
import  urllib.request

global fn
fn = "imgurl.txt"
#获取源码
def getHtml(url):
     res = urllib.request.urlopen(url)
     html = res.read()
     # print(type(html))
     return html

#进度显示
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print ('当前图片下载进度 %.2f%%' % per)

#下载图片
def getImg(html):
    reg = r'img src="(.*?\.jpg)" alt'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    imginfolist = imglist[1:14:1]

    start = time.time()
    x = 0
    for imgurl in imginfolist:
        urllib.request.urlretrieve(imgurl,'E:\codebase\python\zg\source\%s.jpg'%x,Schedule)
        fd = open(fn,"a+")
        fr = fd.write(imgurl)
        fd.write('\n')  # 显示写入换行
        fd.close()
        x = x+1
    c = time.time() - start
    print('下载图片耗时:%0.2f 秒' % (c))

# <img src="http://img08.tooopen.com/20181110/tooopen_sl_142255225556448.jpg" title="闪电图片素材">
htmlsrc = getHtml('http://www.tooopen.com/img/87_312.aspx')
htmlimg = getImg(str(htmlsrc))


