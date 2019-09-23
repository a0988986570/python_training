# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:18:24 2019

@author: user
"""

#網頁資料擷取與分析

#解析網址=>利用python的urllib模組的urlparse函式，可以解析網址=>P5-2
"""
from urllib.parse import urlparse
url="https://www.youtube.com/?gl=TW&hl=zh-TW"
data=urlparse(url)
print(data)
"""

#網頁資料擷取
#匯入requests
import requests
url="https://www.youtube.com/?gl=TW&hl=zh-TW"
html=requests.get(url) #requests.get(url)模擬HTTP GET方法送出一個請求給SEVER，SEVER回應RESPONCE傳入html
html.encoding="utf-8" #設定編碼
#data=html.text => text屬性取得原始碼內容，並為一長串的字串
print(html.text)  #text屬性取得原始碼內容，並為一長串的字串

#取得網頁原始碼後，即可對原始碼加以處理 EX:splitlines()
"""
htmllist=html.text.splitlines() #每一列分割成串列，並去除跳列字元，將結果以list存回
for low in htmllist:
    print(low)
""" 
#尋找指定字串
"""
if "已新增" in html.text:
    print("找到了")
else:
    print("沒有找到")
"""

#尋找指定字串，並記錄出現次數
"""
total=0
htmllist=html.text.splitlines()
for low in htmllist:
    if "已新增" in low:
        total+=1
print("找到{}次!".format(total))
"""


