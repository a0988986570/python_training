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
print(data1)