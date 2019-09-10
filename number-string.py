# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#數字運算
x=3+6
print(x)

x=7/6 #非整數除法
print(x)

x=7//6 #整數除法
print(x)

x=2**3 #次方
print(x)

x=7%3 #取餘數
print(x)

#字串運算
s="Hello"
print(s)
s="Hel\"lo" #加個\作為跳脫，與字串的""做區隔
print(s)

s="hello"+"world" #字串串接
print(s)
s="hello" "world" #python字串串接特殊用法
print(s)

s="hello\nworld" #換行
print(s)
s="""hello
world"""   #換行特殊用法，要3個""" """"
print(s)

s="hello"*3 #字串連續出現3遍(特殊用法)
print(s)

#字串會對內部字元編號(索引)，從0開始算起
s="hello"
print(s[0])
#取子字串
print(s[1:4]) #包含開頭編號，但不包含結尾
print(s[1:]) #開頭編號開始取到全部
print(s[:4]) #取全部但不包含結尾
