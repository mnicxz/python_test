import urllib.request
import requests
import re
import json
import time
from multiprocessing import Pool

# import bs4 from BeautifulSoup
# TODO:找到一个反爬虫的网页
# FIXME:获取微博的源码时会显示编码错误

maoyan = 'https://maoyan.com/board/4?offset='
bilibili = 'https://www.bilibili.com/'
weibo = 'https://weibo.com/?category=0'
pagenum = 10


def getpage(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    page = resp.read().decode("utf-8")
    return page


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.content.decode('utf-8')
        return html
    else:
        return None


def getbody(html):
    body_pattern = re.compile(
        '<dd.*?board-index.*?">(.*?)</i.*?data-src="(.*?)".*?class="name"><a.*?>(.*?)</a.*?class="star">(.*?)</p.*?class="releasetime">(.*?)</p.*?class="score".*?><i class="integer">(.*?).</i><i class="fraction">(.*?)</i></p>', re.S)
    #                       '<dd.*?board-index.*?">(\d+)</i.*?data-src="(.*?)".*?<p class="name"><a.*?>(.*?)</a>.*?<p class="star">(.*?)</p.*?class="releasetime">(.*?)</p.*?</dd>'
    items = re.findall(body_pattern, html)

    results = []
    for item in items:

        results.append({
            '排名': item[0],
            '海报': item[1],
            '名称': item[2],
            '演员': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': int(item[5])+0.1*int(item[6])
        })

    # print(items)
    return results


'''
html = getpage(maoyan)
#result=[]
result = getbody(html)
print("1")
print(result)
'''

def save_all_page(url_base,pagenum):
    for i in range(0,pagenum):
            url=url_base+str(i*10)
            html=getpage(url)
            items=getbody(html)
            for item in items:
                    with open('film.json','a',encoding='utf-8') as f:
                            json.dump(item,f,ensure_ascii=False)


def save_one_page(url):
    html = getpage(url)
    items = getbody(html)
    for item in items:
        with open('film.json', 'a', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False)

##FIXME:当单进程和多进程同时存在时，单进程会重复5次
start = time.time()
print('start')
for i in range(0, pagenum):
    url = maoyan+str(i*10)
    save_one_page(url)
    print(i)
print('end')
end = time.time()
print('单进程用时：',end-start)
'''
if __name__ == "__main__":
    s = time.time()
    pool = Pool()
    for i in range(0, pagenum):
        url= maoyan+str(i*10)
        pool.apply_async(save_one_page, (url,))
    pool.close()
    pool.join()
    e = time.time()
    print('多进程用时：', e-s)
'''