#author:alvin
#coding:utf8
from selenium import webdriver
import  time
# dr = webdriver.Chrome()   # http://chromedriver.storage.googleapis.com/index.html
dr = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
dr.maximize_window()
# print ("设置浏览器宽480、高800显示")
# dr.set_window_size(480, 800)  #参数数字为像素点
time.sleep(2)
dr.get("https://www.baidu.com")
dr.find_element_by_name("wd").send_keys("qatest")
dr.find_element_by_id("su").click()
# dr.forward()
title = dr.title
actitle ="百度一下，你就知道"
print(title)
time.sleep(3)
dr.close()