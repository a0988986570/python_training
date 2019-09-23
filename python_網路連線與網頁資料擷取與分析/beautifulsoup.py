# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:54:40 2019

@author: user
"""

#網頁分析
#使用Beautifulsoup網頁解析模組
"""
相關屬性或方法
tag名稱=>傳回指定tag內容
text=>傳回除去html標籤後的網頁文字內容
find()=>傳回第一個符合條件的tag
find_all()=>傳回所有符合條件的tag
select()=>傳回指定css選擇器如 id("#id")或 class(".class")的內容
"""

import requests as req
from bs4 import BeautifulSoup  #使用Beautifulsoup網頁解析模組
url="http://www.taiwanlottery.com.tw"
htmldata=req.get(url).text
#print(htmldata)
data=BeautifulSoup(htmldata,"html.parser") #html.parse用來解析原始碼
#print(data.title.text) #取得標籤內容

#find隨機尋找一個符合條件的標題，並傳回字串，找不到傳回None
#find_all尋找所有符合條件的標題，傳回串列，找不到傳回空串列
#tag=data.find("div")
#print(tag)
#tag1=data.find_all("div")
#print(tag1)

#tag2=data.find_all("div",{"id":"left"}) #也可以添加屬性內容當參數(此參數為字典)
#print(tag2)
"""
寫法2:
tag2=data.find_all("div",id="left") #也可以添加屬性內容當參數(此參數為字典)
print(tag2)
"""

"""
select()方法=>P5-15
get()方法=>讀取屬性內容 P5-17
"""

#實例練習 P5-18 => 讀取網頁所有<a>超連結，並顯示所有href屬性內容
import requests
from bs4 import BeautifulSoup as bs
url="http://www.e-happy.com.tw"

html=requests.get(url)
html.encoding="utf-8" #編碼
htmldata=html.text
data=bs(htmldata,"html.parser")
link=data.find_all("a")
#print(link)
for l in link:
    href=l.get("href") #取得屬性內容
    if href !=None and href.startswith("http://"):
        print(href)
