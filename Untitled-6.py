'''
    AJAX最大的优点就是在不加载整个网页的情况下，可以与服务器交换数据并更新部分网页
'''

import requests
import json
from multiprocessing import Pool
from urllib.parse import urlencode
'''
from urllib.parser import urlencode 是python2的导入方法
from urllib.parse import urlencode  是python3的导入方法
'''


def get_page_index(offset):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': '足球',
        'count': '20',
        'cur_tab': '1'
    }
    url = 'https://www.toutiao.com/api/search/content/?'+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            #print(response.text)
            with open('soccer.json','w',encoding='utf-8') as f:
                f.write(response.text)
            return response.text
        else:
            print('E')
            return None
    except Exception:
        print('Error')
        return None

def parse_page_index(html):
    data=json.loads(html)
    results=[]
    if data and 'data' in data.keys():
        for item in data.get('data'):
            article_url=item.get('article_url')
            if article_url and ('group' in article_url):
                results.append(article_url)
    return results
'''
html=get_page_index(20)
for url in parse_page_index(html):
    print(url)
'''

def main(offset):
    html=get_page_index(offset)
    for url in parse_page_index(html):
        print(url)

if __name__=='__main__':
    p=Pool()
    p.map(main,[i*20 for i in range(3)])