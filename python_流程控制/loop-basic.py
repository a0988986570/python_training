# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:00:14 2019

@author: user
"""

#while迴圈

n=1
while n<=3:
    print(n)
    n+=1

#1+2+3+...+10
n=1
total=0 #紀錄累加成果
while n<=10:
    total=total+n
    n+=1
print(total)
    

#for迴圈
for x in[3,5,1]:
    print(x)
for x in "Hello":
    print(x)
for x in range(5):
    print(x)
for x in range(5,10):
    print(x)

#1+2+3+...+10
total=0
for x in range(1,11):
    total=total+x
print(total)
    