# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:01:27 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
#1、建立資料集
def createdata():
    samples=np.array([[3,-3],[4,-3],[1,1],[1,2]])
    labels=[-1,-1,1,1]
    return samples,labels
#訓練感知機模型
class Perceptron:
    def __init__(self,x,y,a=1):
        self.x=x
        self.y=y
        self.w=np.zeros((x.shape[1],1))#初始化權重，w1,w2均為0
        self.b=0
        self.a=1#學習率
        self.numsamples=self.x.shape[0]
        self.numfeatures=self.x.shape[1]
        def sign(self,w,b,x):
            y=np.dot(x,w)+b
            return int(y)
        def update(self,label_i,data_i):
            tmp=label_i*self.a*data_i
            tmp=tmp.reshape(self.w.shape)
#更新w和b
self.w=tmp self.w
self.b=self.b label_i*self.a
def train(self):
isFind=False
while not isFind:
count=0
for i in range(self.numsamples):
tmpY=self.sign(self.w,self.b,self.x[i,:])
if tmpY*self.y[i]<=0:#如果是一個誤分類例項點
print '誤分類點為：',self.x[i,:],'此時的w和b為：',self.w,self.b
count =1
self.update(self.y[i],self.x[i,:])
if count==0:
print '最終訓練得到的w和b為：',self.w,self.b
isFind=True
return self.w,self.b
#畫圖描繪
class Picture:
def __init__(self,data,w,b):
self.b=b
self.w=w
plt.figure(1)
plt.title('Perceptron Learning Algorithm',size=14)
plt.xlabel('x0-axis',size=14)
plt.ylabel('x1-axis',size=14)
xData=np.linspace(0,5,100)
yData=self.expression(xData)
plt.plot(xData,yData,color='r',label='sample data')
plt.scatter(data[0][0],data[0][1],s=50)
plt.scatter(data[1][0],data[1][1],s=50)
plt.scatter(data[2][0],data[2][1],s=50,marker='x')
plt.scatter(data[3][0],data[3][1],s=50,marker='x')
plt.savefig('2d.png',dpi=75)
def expression(self,x):
y=(-self.b-self.w[0]*x)/self.w[1]#注意在此，把x0，x1當做兩個座標軸，把x1當做自變數，x2為因變數
return y
def Show(self):
plt.show()
if __name__ == '__main__':
samples,labels=createdata()
myperceptron=Perceptron(x=samples,y=labels)
weights,bias=myperceptron.train()
Picture=Picture(samples,weights,bias)
Picture.Show()