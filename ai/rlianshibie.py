# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 15:11
# @Author  : alvin
# @File    : rlianshibie.py
# @Software: PyCharm
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2(9).xml')
frame = cv2.imread(r'timg.jpg')
gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
cv2.waitKey(0)
for (x,y,w,h) in faces:
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    print(frame)
# 显示图片
cv2.imshow('v',frame)
cv2.waitKey(0)
# while True:
#     ret,frame =
