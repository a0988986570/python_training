# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:22:51 2019

@author: user
"""

#定義類別、與類別屬性(類別屬性:封裝在類別中的變數和函式)
#定義一個類別 IO，有2個屬性 supportedSrcs和 read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not support")
        else:
            print("Read from",src)

#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")