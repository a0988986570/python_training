# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:20:06 2019

@author: user
"""

#break的簡易範例
n=0
while n<5:
    if n==3:
        break
    print(n) #印出迴圈中的n
    n+=1
print("最後的n:",n) #印出迴圈結束後的n

#continue的簡易範例
n=0
for x in [0,1,2,3]:
    if x%2==0:  #x是偶數
        continue
    print(x)
    n+=1
print("最後的n:",n)
    
#else的簡易範例(else:迴圈結束前，執行此區塊的命令)
sum=0
for n in range(11):
    sum+=n
else:
    print(sum) #印出1+2+3+...+10的結果

#綜合範例:找出整數平方根
#輸入9，得到3
#輸入11，得到[沒有]整數的平方根
n=input("請輸入一個正整數:")
n=int(n) #將字串轉為整數
for i in range(n): #i從0~n-1
    if i*i==n:
        print("整數平方根:",i)
        break #用break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根")
    
    