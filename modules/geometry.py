# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:45:08 2019

@author: user
"""

#在 geometry模組中定義幾何運算功能
def distance(x1,y1,x2,y2): #兩點距離
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def slope(x1,y1,x2,y2): #斜率
    return (y2-y1)/(x2-x1)