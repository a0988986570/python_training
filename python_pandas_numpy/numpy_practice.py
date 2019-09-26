# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:40:55 2019

@author: user
"""

"""
網址:https://blog.techbridge.cc/2017/07/28/data-science-101-numpy-tutorial/

Numpy 陣列
Numpy 的重點在於陣列的操作，其所有功能特色都建築在同質且多重維度的 ndarray（N-dimensional array）上。ndarray 的關鍵屬性是維度（ndim）、形狀（shape）和數值類型（dtype）。 一般我們稱一維陣列為 vector 而二維陣列為 matrix。一開始我們會引入 numpy 模組，透過傳入 list 到 numpy.array() 創建陣列。
"""


# 引入 numpy 模組
import numpy as np
np1 = np.array([1, 2, 3])
np2 = np.array([3, 4, 5])

# 陣列相加
print(np1 + np2) # [4 6 8]

# 顯示相關資訊
print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別

#np=np.array([[1,2,3],[1,2,3]])
#print(np)
"""
#從檔案取資料
npd = np.genfromtxt('data.csv', delimiter=',')
"""


#改變陣列維度
np3 = np.array([1, 2, 3, 4, 5, 6])
np3 = np3.reshape([2, 3]) #[列，行]
print(np3,np3.ndim, np3.shape, np3.dtype) # 2 (2, 3) int64


"""
改變陣列型別（bool、int、float、string）：

bool 可以包含 True、False，int 可以包含 int16、int32、int64。其中數字是指 bits。float 可以包含 16、32、64 表示小數點後幾位。string 可以是 string、unicode。nan 則表示遺失值。
"""
np3 = np3.astype('int32')
print(np3.dtype)
# dtype('int64')


#建立陣列
#建立填滿 0 或 1 的陣列：
np4 = np.zeros([2, 3]) 
# array([[ 0.,  0.,  0.], [ 0.,  0.,  0.]])
np5 = np.ones([2, 3]) 
# array([[ 1.,  1.,  1.], [ 1.,  1.,  1.]])
print(np4,np5,sep="\n")



#陣列索引與切片
#一維陣列操作和 Python 原生 list 類似
np6 = np.array([1, 2, 3, 4, 5, 6])
print(np6[2]) # 3
#二維陣列
np6 = np6.reshape([2, 3])
print(np6[1, 0]) # 4



#使用布林遮罩來取值
np7 = np.array([1, 2, 3, 4, 5, 6])
print(np7 > 3) # [False False False  True  True  True]
print(np7[np7 > 3]) # [4 5 6]

np7 = np7.reshape([2, 3])
print(np7.sum(axis=1)) # 將 axis=1 橫向加總 [6 15]


#numpy axis概念整理筆記
#網址:http://changtw-blog.logdown.com/posts/895468-python-numpy-axis-concept-organize-notes
"""
axis1=>column
axis0=>row
"""

nd = np.arange(1,10).reshape(3,3)
#print(nd)
print(nd[0],nd[0][:])
"""
nd[0]:表示取軸0的第0項
nd[0][:]:取軸0第0項然後對應的軸1每項都要
所以nd[0]與nd[0][:]取的東西相同
"""
print(nd[0][1]) #先選取軸0的第0項,接著再對應取軸1的第1項

print(nd[:,0:2] ) #表示軸0的項目全部都要,但只取每一項的軸1的0到1項

print(nd.sum(axis=1))
#表示將軸1的各項相加,但不將軸0合併(合併了軸0就等於一般ndarray.sum()的結果了),也就是軸0的各項分別各自將其軸1各項相加(每列各自將其對應軸0各項相加)
print(nd.sum())
