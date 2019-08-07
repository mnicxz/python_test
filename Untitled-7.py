import requests
from bs4 import BeautifulSoup
import re

"""
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        else:
            return None
    except Exception:
        print('请求索引页出错！')
        return None

def main(offset):
    html=get_page_index(offset)
    for url in parse_page_index(html):
        content=get_page_detail(url)
        parse_page_detail(content)

if __name__=='__main__':
    # p=Pool()
    # p.map(main,[i*20 for i in range(3)])
    for i in range(3):
        main(i*20)

"""

def get_html(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception:
        print("request html error")
        return None

def parse_html(html):
    soup=BeautifulSoup(html,'lxml')
    return soup

url ="https://www.toutiao.com/a6706791171974234637/"
html = get_html(url)
soup=parse_html(html)
print(soup)

