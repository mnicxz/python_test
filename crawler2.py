# 爬虫实战【2】Python博客园-获取某个博主所有文章的URL列表
import urllib.request
import re
from bs4 import BeautifulSoup

# 该作者的随笔有多少页
pagenum = 7
url = 'https://www.cnblogs.com/xingzhui/p/?page='
url1 = 'https://www.cnblogs.com/xingzhui/p/7881262.html'


def get_html(url):
    res = urllib.request.urlopen(url)
    html_page = res.read().decode('utf-8')
    return html_page


def get_urls(url, pagenum):
    total_urls = []
    for i in range(1, pagenum+1):
        url_1 = url+str(i)
        html = get_html(url_1)
        # print(html)
        pattern = r'<div class="postTitl2".*href="(.*)">.*</a>'
        urls = re.findall(pattern, html)
        for url_ in urls:
            total_urls.append(url_)
        # print(urls,'\n')
        # print(href,":",title)
        # print(total_urls.__len__())
    return total_urls

# 获取每个随笔的标题
def get_title(url):
    html = get_html(url)
    title_pattern = r'<a.*id="cb_post_title_url".*>(.*)</a>'
    title_match = re.search(title_pattern, html)
    title = title_match.group(1)
    return title

# 获取每个随笔的内容


def get_content(url):
    html = get_html(url)
    # title_pattern=r'<a.*id="cb_post_title_url".*>(.*)</a>'
    #title_match= re.search(title_pattern,html)
    #title = title_match.group(1)
    # return title
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find(id="cnblogs_post_body")
    return div


newurls = get_urls(url, pagenum)
i = 0
for urls in newurls:
    title = get_title(urls)
    content = get_content(urls)
    filename = title+'.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content.text)

print("success")  
