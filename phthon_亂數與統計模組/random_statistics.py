# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:50:48 2019

@author: user
"""

#隨機模組
import random
#隨機選取
data=random.choice([1,5,6,10,20])
print(data)

data=random.sample([1,5,6,10,20],3)
print(data) #sample可用來挑選n筆data，且回傳列表

#隨機調換順序(就是洗牌的概念)
data=[1,5,8,20]
random.shuffle(data) #shuffle用來隨機就地調換資料順序
print(data)

#隨機取得亂數
data=random.random() #0.0~1.0之間的隨機亂數
print(data)
#uniform強調數字之間出現的機率相同
data=random.uniform(0.0,1.0) 
print(data)
#且uniform可指定範圍
data=random.uniform(60,100) #60-100之間的隨機亂數
print(data)

#取得常態分配亂數 (平均數,標準差)
#取得平均數100、標準差10的常態分配亂數
data=random.normalvariate(100,10)
print(data) #平均數100、標準差10，得到的資料多數在90-110之間

#取得平均數0、標準差5的常態分配亂數
data=random.normalvariate(0,5)
print(data) #平均數0、標準差5，得到的資料多數在-5~5之間

#統計模組
import statistics as stat

data=stat.mean([1,4,5,8])#取Mean
print(data)

data=stat.median([1,2,3,4,5,8,100])#取Median
print(data)

data=stat.stdev([1,2,3,4,5,8,10])#取標準差
print(data)