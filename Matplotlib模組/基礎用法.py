# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:46:17 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np


"""
linspace、plot、show()用法
"""
#在-1~1之間，平均生成50個點(包含-1、1)
x=np.linspace(-1,1,50)
#y=2*x+1
y=x**2
plt.plot(x,y) 
#plot就是展示x與y座標的值,並用"線"表示
plt.show() #展示圖型


"""
1、figure:框架
2、線顏色、線寬、樣式設定
"""
x=np.linspace(-1,1,50)
y1=2*x+1
y2=x**2

#做出2個框架
#框架1
plt.figure()
plt.plot(x,y1) 
plt.show() 
#框架2
plt.figure(figsize=(8,5)) #figsize(長，寬)，給定框架大小
plt.plot(x,y2)
#給予第2條線，並設定顏色、線寬、線樣式
plt.plot(x,y1,color="red",lw="1.0",ls="--")
plt.show()


"""
坐標軸設置
1、坐標軸範圍(xlim,ylim)
2、坐標軸名稱(xlabel,ylabel)
3、座標軸小標單位(plt.xticks,plt.yticks)
4、座標軸位置(ax=plt.gca(),ax.spines)
"""
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color="red",lw=1.0,ls="--")

plt.xlim (-1,2) #設置X軸範圍
plt.ylim (-2,3) #設置Y軸範圍
plt.xlabel("I am x") #設置X軸名稱
plt.ylabel("I am y") #設置Y軸名稱

#設置座標軸小標單位
new_ticks=np.linspace(-1,2,5)
#print(new_ticks)
#設置X軸座標小標單位
plt.xticks(new_ticks)
#設置Y軸座標小標單位(可換為文字)
plt.yticks([-2,-1.8,-1,1.22,3],["really bad","bad","normal","good","really good"])

#設置座標軸位置
#gca="get current axis"
ax=plt.gca()
#spines就是4個邊框
ax.spines["right"].set_color("none") #將右邊框取消
ax.spines["top"].set_color("none") #將上邊框取消
ax.xaxis.set_ticks_position("bottom") #將下邊框當作X軸
ax.yaxis.set_ticks_position("left") #將左邊框當作X軸
ax.spines["bottom"].set_position(("data",0)) #將下邊框以Y軸data做定位，設在Y軸data=0的位置
ax.spines["left"].set_position(("data",0)) #將左邊框以X軸data做定位，設在X軸data=0的位置
#定位方法還有outward,axes...(自行研究)

"""
legend:圖例教學
"""
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.xlim (-1,2) 
plt.ylim (-2,3) 
plt.xlabel("I am x") 
plt.ylabel("I am y")
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],["really bad","bad","normal","good","really good"]) 

plt.plot(x,y2,label="up")
#label用來給予圖例名字
plt.plot(x,y1,color="red",lw=1.0,ls="--",label="down")
plt.legend() 
#顯示圖例(handles,labels,loc...都是可調參數)


"""
添加註解
"""
x=np.linspace(-3,3,50)
y=2*x+1

plt.figure()
plt.plot(x,y)

ax=plt.gca()
ax.spines["right"].set_color("none") 
ax.spines["top"].set_color("none") 
ax.xaxis.set_ticks_position("bottom") 
ax.yaxis.set_ticks_position("left") 
ax.spines["bottom"].set_position(("data",0)) 
ax.spines["left"].set_position(("data",0))

x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color="b") #scatter用來展示圖型，並用"點"描述
plt.plot([x0,x0],[y0,0],"k--",lw=2.5) 
#"k--"簡寫帶表黑色虛線
#上述即是(x0,y0)與(x0,0)這兩點所成的線

#註解方法一
plt.annotate("2x+1=%s"%y0,xy=(x0,y0),xycoords="data",xytext=(+30,-30),textcoords="offset points",fontsize=16,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2")
)


#註解方法二
plt.text(-3.7,3,"Thisisthemethod",fontdict={"size":16,"color":"r"})
plt.show() 








