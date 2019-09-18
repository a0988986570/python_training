# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:27:11 2019

@author: user
"""

#儲存檔案
#基本語法 => 檔案物件=open(檔案路徑，mode=開啟模式,encoding="utf-8") #utf-8中文編碼
#開啟模式(讀取=>-r,寫入=>-w,讀寫=>-r+)
file=open("data.txt",mode="w") # 開啟一個data.txt檔
file.write("hello\nSecond line\n測試中文") #操作
file.close() #關閉

#最佳實務寫法，會自動close檔案
with open("data1.txt",mode="w") as file:
    file.write("最佳實務寫法")
 
with open("data2.txt",mode="w") as file:
    file.write("5\n3")
    
#讀取檔案
with open("data.txt",mode="r") as file:
    data=file.read()
print(data)

#把檔案中的數字資料，一行一行讀取出來，並計算總合
sum=0
with open("data2.txt",mode="r") as file:
    for line in file: #一行一行讀取(string型態)
        sum+=int(line)
print(sum)
    
#使用JSON格式讀取、複寫檔案
import json
#從檔案中讀取JSON資料，放入變數data裡面
with open ("config.json",mode="r") as file:
    data=json.load(file)  #JSON格式讀取 "json.load"
print(data) #data是一個"字典"資料
print("name",data["name"])
print("version",data["version"])

data["name"]="New Name" #修改變數data中的資料
#把最新的資料複寫回檔案中
with open ("config.json",mode="w") as file:
    json.dump(data,file) #JSON格式複寫 "json.dump"

