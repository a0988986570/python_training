# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:02:34 2019

@author: user
"""

#載入matplotlib模組
import matplotlib.pyplot as plt

"""
#matplotlib繪圖組要功能為繪製x,y座標圖，必須將x,y座標存在串列傳給matplotlib製圖
#x,y元素數目需相同
listx=[1,5,7,9,13,16]
listy=[15,50,80,40,70,50]
listx1=[3,8,10,12,16,19]
listy1=[18,53,83,43,73,53]
#matplotlib.pyplot線性繪圖方法為plot
#語法:模組名稱.plot(x座標串列,y座標串列) =>用來繪製線性圖
plt.plot(listx,listy)
plt.plot(listx1,listy1) #一個圖表可以繪製多個圖形，通常會將所有圖形繪製在顯示
plt.show() #顯示繪圖結果
#其他參數
plt.plot(listx,listy,color="red",lw=5,ls="--",label="title name")
plt.legend() #label需搭配 plt.legend() 才會顯示
plt.show()
"""

#實例練習 課本p7-7
listx=[1,5,7,9,13,16]
listy=[15,50,80,40,70,50]
plt.plot(listx,listy,label="Male")
listx1=[3,8,10,12,16,19]
listy1=[18,53,83,43,73,53]
plt.plot(listx1,listy1,color="red",lw=5,ls="--",label="Female")
plt.title("Pocket Money") #圖表標題
plt.xlabel("年紀")  #x座標標題
plt.ylabel("錢") #y座標標題
plt.xlim(0.0,20.0) #設定x座標範圍
plt.ylim(0,100) #設定y座標範圍
plt.legend() #用來顯示圖例
plt.show()
