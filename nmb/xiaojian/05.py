#author:alvin
#coding:utf8
from selenium import webdriver
import  time
# dr = webdriver.Chrome()   # http://chromedriver.storage.googleapis.com/index.html
dr = webdriver.Firefox()
dr.maximize_window()
# print ("设置浏览器宽480、高800显示")
# dr.set_window_size(480, 800)  #参数数字为像素点
time.sleep(1)
start_time = time.time()
dr.get("https://www.baidu.com")
dr.find_element_by_name("wd").send_keys("qatest")
dr.find_element_by_id("su").click()
end_time=  time.time() -start_time
print(end_time)
# dr.forward()
title = dr.title
actitle ="百度一下，你就知道"
assert  actitle in title
print("is running ok!")
dr.close()