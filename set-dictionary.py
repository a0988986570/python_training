# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:40:02 2019

@author: user
"""
#集合的運算
s1={3,4,5}
print(3 in s1) #判斷元素是否存在集合裡
print(3 not in s1)

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集: &
print(s3)

s3=s1|s2 #聯集: |
print(s3)

s3=s1-s2 #差集:從S1中減去和S2重疊的部分
print(s3)

s3=s1^s2 #反交集;取2個集合中不重疊部分
print(s3)

s=set("Hello") #把字串差解成集合:set(字串)
print(s)

#字典的運算:key-value配對
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])

print("apple" in dic) #判斷key是否存在

del dic["apple"] #刪除字典中的鍵值對(key-value pair)
print(dic)

#由列表資料產生字典
dic={x:x*2 for x in [3,4,5]}
print(dic)

