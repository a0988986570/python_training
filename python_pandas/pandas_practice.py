# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:34:22 2019

@author: user
"""

#Pandas基本操作
"""
Pandas兩個重要概念:
    1.Series:單維度的資料
        建立Series=>
            #載入Pandas模組
            import pandas as pd
            #以"列表"資料為底，建立Series
            pd.Series(列表)
    2.DataFrame:雙維度的資料
        建立DataFrame=>
            #載入Pandas模組
            import pandas as pd
            #以"字典"資料為底，建立DataFrame
            pd.DataFrame(字典)
"""        

#載入pandas模組
import pandas as pd

#建立Series
data=pd.Series([20,10,15])
 
#基本series操作
#print(data)
#print("Max",data.max()) #最大值
#print("Medium",data.median()) #中位數
#data=data*2
#print(data) #所有資料*2

#特殊比較用法=>在未來進階操作很常用到
data=data==20 #data series內有沒有資料(data)==20,將比較完的結果回傳給data
print(data)
 
#建立DataFrame
data=pd.DataFrame({
         "name":["Amy","John","Bob"],
         "salary":[30000,50000,40000]
         })
#基本DataFrame操作
print(data)
#取得特定的欄位(直行)
print(data["name"])
#取得特定的列(橫列)，從編號0開始
print(data.iloc[0]) #印出第一列
print(data.iloc[1]) #印出第二列