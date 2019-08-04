# 爬取哔哩哔哩国创排行
# 练手之作
#测试 test_git

import re
import requests
import urllib.request
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
'''
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
        #此方法可以爬取
        #req=urllib.request.Request(url,headers=headers)
        #resp=urllib.request.urlopen(req)
        #html=resp.read()
        #return html

    except Exception:
        print("Error!")


#获取国创排行网址

url='https://www.bilibili.com/'
html=get_html(url)
#print(html)

with open('bilibili.txt','w',encoding='utf-8') as f:
    f.write(html)
    print('done')

'''

# 使用selenium及webdriver爬取
option=webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=option)

keyword = 'guochuang'
url = 'https://www.bilibili.com/'+keyword

# browser.get(url)

# 获取首页


def get_page(url):
    try:
        browser.get(url)
        page = browser.page_source  # 获取源码
        return page
    except Exception:
        print("Error!!!")


if __name__ == '__main__':
    html = get_page(url)
    soup = BeautifulSoup(html,'lxml')
    infos = soup.find_all(class_='rank-item')
    '''
    for info in infos:
        title = info.find('a').get('title')
        href = info.find('a').get('href')
        print('标题：{title}，链接：{href}')'''

    print(infos)
