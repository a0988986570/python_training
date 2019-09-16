# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:32:11 2019

@author: user
"""
#參數的預設資料:當呼叫函式沒有給參數值，即可使用預設資料
def power(base,exp=0): #若有給預設值
    print(base**exp)
power(3,2)
#power(4) 忘了寫第2個參數結果出錯
power(4) #exp有給預設值0，程式正確

#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4) #使用參數名稱對應

#無限/不定(*參數名稱) 參數資料
def avg(*ns): #參數以tuple的型態傳入儲存
    #print(ns) #印出tuple
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))
    
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)