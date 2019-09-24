# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:36:44 2019

@author: user
"""

#網路爬蟲
#取得台灣彩券威力彩最新開獎結果
#實例練習 P5-19

import requests as req
from bs4 import BeautifulSoup as bs
url="https://www.taiwanlottery.com.tw/"
html=req.get(url)
html.encoding="utf-8"
htmldata=html.text
#print(htmldata)
data=bs(htmldata,"html.parser")

data1=data.select("#rightdown") #找到id="rightdown"的標籤儲存成List，傳回data1
#print(data1)
data2=data1[0].find("div",{"class":"contents_box02"})
#print(data2)
data3=data2.find_all("div",{"class":"ball_tx ball_green"})
#print(data3)
print("開出順序:",end=" ") #end結束字元，預設為"\n"
for n in range(0,6):
    print(data3[n].text,end=" ")
print("")
print("大小順序:",end=" ")
for n in range(6,12):
    print(data3[n].text,end=" ")
print("")
print("第2區:",data2.find("div",{"class":"ball_red"}).text)