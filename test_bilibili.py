#爬取哔哩哔哩国创排行
#虽然单单爬取最新排行毫无用处，亦或是我现在找不到任何用处，但还是先来练练手

import re
import requests
import urllib.request
import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Except
import csv

#获取网站首页
def get_html(url):
    try:
        headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/74.0.3729.157 Safari/537.36'}
        #可用，但只可获取源代码
        resp=requests.get(url,headers=headers).text
        return resp
        #存在问题，无法爬取哔哩哔哩首页
        #if resp.status_codes==200:
        #   html=resp.content.decode('utf-8')
        #    return html
        #else:
        #    return None 
        '''#此方法可以爬取
        req=urllib.request.Request(url,headers=headers)
        resp=urllib.request.urlopen(req)
        html=resp.read()
        return html
        '''
    except Exception:
        print("Error!")


#获取国创排行网址

#url='https://www.bilibili.com/'
#html=get_html(url)
#print(html)
'''
with open('bilibili.txt','w',encoding='utf-8') as f:
    f.write(html)
    print('done')
'''

#使用selenium+webdriver获取哔哩哔哩国创首页当日排行
url='https://www.bilibili.com/guochuang/'
option=webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
browser=webdriver.Chrome(chrome_options=option)
browser.get(url)
Wait(browser,100).until(Except.presence_of_all_elements_located)
'''
data=browser.find_element_by_xpath('//*[@id="app"]/div[5]/div[2]').find_elements_by_tag_name('li')
for i in range(len(data)):
    text=data[i].find_elements_by_class_name('title').text
    print(text)
print(data)
'''
with open("bilibili.txt","w",encoding="utf-8") as f:
    f.write(browser.page_source)
f.close()