# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:36:15 2019

@author: user
"""

#網路連線
#import urllib.request as request
#src="https://www.youtube.com/?gl=TW&hl=zh-TW"
#with request.urlopen(src) as response:  #與取得file的方法一樣
#    data=response.read().decode("utf-8") #取得網頁的原始碼,並用utf-8去做解碼(可以解決中文字亂碼問題)
#print(data)

#串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
#print(data)

#將公司名稱列表出來
clist=data["result"]["results"]
#print(clist)
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")

