#author:alvin
#coding:utf8
from selenium import webdriver
import  time
# dr = webdriver.Chrome()   # http://chromedriver.storage.googleapis.com/index.html
dr = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
dr.maximize_window()
time.sleep(2)
dr.get("https://www.baidu.com")
dr.find_element_by_id("su").send_keys("autotest")