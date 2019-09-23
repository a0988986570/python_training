# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:08:06 2019

@author: user
"""

#使用正規表示式擷取網頁內容:因為有些字串過於複雜，不容易用 in 完成搜尋，例如:電子郵件、電話號碼... =>P5-6~5-10
#匯入 regular expression
import re
pat=re.compile("[a-z]+")

#match()法=>傳回指定的字串中符合正規表示式的字串，直到不符合字元(從第一個字元開始看起，所以若第一個字元不是正規表示式的字串，及傳回None)
m=pat.match("tem12po") #會回傳<re.Match object; span=(0, 3), match='tem'>物件
print(m)
print(m.group()) #回傳找到的match字串
print(m.start()) #回傳match的開始位置
print(m.end()) #回傳match的結束位置
print(m.span()) #回傳match的(開始位置,結束位置)

#re.match()方法=>簡化用法
m=re.match(r"[a-z]+","tem12po") #習慣在第一個參數前加一個r，告知為整規表示式
print(m)

#search()法=>傳回指定的字串中第一組符合正規表示式的字串，若無符合字元，傳回None
m=re.search(r"[a-z]+","3tem12po") #此例若用match()法則傳回None
print(m)

#findall()=>傳回指定的字串中所有符合正規表示式的字串，並傳回串列
m=re.findall(r"[a-z]+","3tem12po")
print(m)


print("-------------------------------")

#實際例子，讀取中華電信"https://auth.cht.com.tw/ldaps/"網站中所有E-mail帳號
import requests as req
import re
html=req.get("https://auth.cht.com.tw/ldaps/")
data=html.text
list=re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9\._]+",data)
for li in list:
    print(li)
