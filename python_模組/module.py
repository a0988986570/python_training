# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:04:17 2019

@author: user
"""

#載入內建的sys模組並取得資訊
#import sys
#print(sys.platform)
#print(sys.maxsize)

#import sys as s #給予載入的模組別名
#print(s.platform)
#print(s.maxsize)

#建立geometry模組，載入使用
#import geometry
#result=geometry.distance(1,1,5,5)
#print(result)
#result=geometry.slope(1,2,5,6)
#print(result)

#調整搜尋模組的路徑
#import sys
#print(sys.path) #印出模組的搜尋路徑[以列表(list)形式存在]

import sys
#在模組的搜尋路徑列表中[新增路徑]
sys.path.append("modules") #將modules這個資料夾放入當前這個路徑(path)，才可以確保載入在modules資料夾內的"geometry"模組
print(sys.path) #印出模組的搜尋路徑列表
print("-----------")
import geometry
print(geometry.distance(1,1,5,5))