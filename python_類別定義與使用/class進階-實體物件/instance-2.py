# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:22:49 2019

@author: user
"""
#此篇教導"實體方法"
#實體方法:封裝在實體物件中的函式
"""
class 類別名稱:
    #定義初始化函式
    def__init__(self):
        定義實體屬性(封裝在實體物件中的變數)
    #定義實體方法(函式)
    def 方法名稱(self,更多自訂參數):
        方法主體，透過self操作實體物件
#建立實體物件，放入變數obj中
obj=類別名稱()
"""

#Point 實體物件的設計:平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #定義實體方法
    def show(self):
        print(self.x,self.y)
    def distance(self,targexX,targexY): #求實體物件座標與目標座標的距離
        return (((self.x-targexX)**2)+((self.y-targexY)**2))**0.5
p=Point(3,4)
p.show() #呼叫實體方法
print(p.distance(0,0)) #計算座標(3,4)和座標(0,0)之間的距離



#File 實體物件的設計:包裝檔案讀取的程式
class File:
    #初始化函式
    def __init__(self,name):
        #兩個實體屬性為name與file
        self.name=name
        self.file=None #尚未開啟檔案:初期設為None
    #實體方法(函式)
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第1個檔案
f1=File("data1.txt") #建立實 體物件放在變數f1
f1.open()
print(f1.read())
#讀取第2個檔案
f2=File("data2.txt") #建立實 體物件放在變數f1
f2.open()
print(f2.read())