# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:40:30 2019

@author: user
"""

#此篇教導"實體物件"和"實體屬性"

# Point 實體物件的設計:平面座標上的點
class Point:
    #定義初始化函式
    def __init__(self,x,y): #透過操作self來定義實體屬性，並可放入初始化參數
        #有x,y兩個實體屬性
        self.x=x
        self.y=y
#建立第一個實體物件，放入變數p1
p1=Point(3,4) #呼叫初始化函式，並直接傳入參數資料
print(p1.x,p1.y)
#建立第二個實體物件
p2=Point(5,6)
print(p2.x,p2.y)


#FullName 實體物件的設計:分開紀錄姓、名資料的全名
class Fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=Fullname("sss","aaa")
print(name1.first,name1.last)
name2=Fullname("aaa","sss")
print(name2.first,name2.last)

        