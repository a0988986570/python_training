# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:26:40 2019

@author: user
"""

#定義函示
#函示內部的程式碼，若是沒有做函示呼叫，就不會執行
def multipy(n1,n2):
    print(n1*n2)
    #return 10
    return n1*n2
#呼叫函示
x=multipy(3,4)
print(x) #函示所得到的值為return回傳的東西，沒有寫return即回傳NONE值

#例子
def multipy1(n1,n2):
    return n1*n2
value=multipy1(3,4)+multipy1(10,5)
print(value)


#函示可用來做程式的包裝:即同樣的事情可交由函示去做
def calculate(max):
    sum=0
    for n in range(1,max+1): #1+...+max
        sum=sum+n
    print(sum)
    
calculate(10)
calculate(20)