# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#有序可變動列表 List
grades=[12,60,15,70,90]
print(grades)
print(grades[3])
grades[0]=55 #把55放到列表第一個位置
print(grades)

print(grades[1:4]) #與string的概念一樣
grades[1:4]=[] #連續刪除列表中從編號1到編號4(不包括)的資料
print(grades)

grades=grades+[12,33] #列表串接
print(grades)

length=len(grades) #取得列表長度
print(length)

#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0][1])
print(data)
data[0][0:2]=[5,5,5]
print(data)

#有序不可變動列表 Tuple
data=(1,2,3)
print(data[0:2])

#data[0]=5 #錯誤:Tuple的資料不可變動

