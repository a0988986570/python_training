# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:28:17 2019

@author: user
"""
#爬蟲教學:https://www.youtube.com/watch?v=9Z9xKWfNo7k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=19
#爬蟲:抓取網站資料=>關鍵心法=>盡可能地讓程式模仿一個普通使用者的樣子

"""
資料解析
=>JSON格式資料:使用內建的json模組即可
=>HTML格式資料:使用第3方套件BeautifulSoup來做解析
"""

#抓取PTT電影版的網頁原始碼(HTML)
"""
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
print(data)

結果出現:HTTPError: Forbidden
連線被禁止=>因為PTT覺得我不是一個正常使用者
"""
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request物件，附加Request Headers的資訊(讓程式像普通使用者)
#Headers的資訊最重要的是"User-Agent"，它會讓網頁伺服器知道我們是使用甚麼瀏覽器、作業系統...
request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        })
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)


#解析原始碼，取得每篇文章的標題
#讓BeautifulSoup協助做解析
import bs4
#root代表整個網頁
root=bs4.BeautifulSoup(data,"html.parser") #html.parser說明data為html
#root.title為抓到網頁title整個標籤(tag)
print(root.title)
# .string為抓標籤內的文字
print(root.title.string)

#find隨機尋找一個符合條件的標題
#find_all尋找所有符合條件的標題
titles=root.find_all("div",class_="title") #尋找class="title"的div標籤
print(titles)
#print(titles.a.string) 會出錯，因為有些title下的沒有a標籤
for title in titles:
    if title.a !=None: #如果標題包含a標籤(沒有被刪除)，印出來
        print(title.a.string)
