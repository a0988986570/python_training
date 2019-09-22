# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:30:36 2019

@author: user
"""

#Flask網站架設-基礎環境建置
"""
流程:
    1.安裝Flask套件
    2.建立專案資料夾，撰寫程式
    3.啟動伺服器，測試網站運作
"""

from flask import Flask
app=Flask(__name__) 
#__name__代表目前執行的模組(app.py)(詳細資料請自行google)

"""
@app.route
函式的裝飾(Decorator):已函式為基礎，提供附加的功能
"""
@app.route("/") #"/"只會在函式的根目錄執行(執行的內容為home())
def home():
    return "Hello Flask!"

@app.route("/test") #代表我們要處理的網站路徑(執行的內容為test())
def test():
    return "This is Test!"

if __name__=="__main__": #如果以app.py為主程式執行
    app.run() #立刻啟動伺服器

