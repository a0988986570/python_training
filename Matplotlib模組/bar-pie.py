# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:38:17 2019

@author: user
"""

#模組名稱.bar(x座標串列,y座標串列,其他參數) =>繪製柱狀圖
#模組名稱.pie(x座標串列,y座標串列,其他參數) =>繪製圓餅圖


import matplotlib.pyplot as plt

#實例練習bar 課本7-7
listx=[1,5,7,9,13,16]
listy=[15,50,80,40,70,50]
listx1=[3,8,10,12,16,19]
listy1=[18,53,83,43,73,53]
plt.bar(listx,listy,label="男性")
plt.bar(listx1,listy1,color="red",label="女性")
plt.legend()
plt.title("零用金統計")
plt.xlabel("年齡")
plt.ylabel("零用錢數目")
plt.xlim(0.0,20.0)
plt.ylim(0,100)
plt.show()

#實例練習pie 課本7-9
labels=["東部","南部","北部","中部"]
sizes=[5,10,20,15]
colors=["red","green","blue","yellow"]
explode=(0,0,0.05,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,labeldistance=1.1,autopct="%2.2f%%",shadow=True,startangle=90,pctdistance=0.6)
plt.axis("equal") #正圓形
plt.legend()
plt.show()


