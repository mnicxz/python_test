#爬虫实战【1】使用python爬取博客园的某一篇文章
import urllib
import re
from bs4 import BeautifulSoup

url = 'https://www.cnblogs.com/xingzhui/p/7881262.html'
res = urllib.request.urlopen(url)
html_page = res.read().decode('utf-8')

title_pattern = r'(<a.*id="cb_post_title_url".*>)(.*)(</a>)'
title_match = re.search(title_pattern,html_page)
title = title_match.group(2)
print(title)
'''
soup = BeautifulSoup(html_page,'html.parser')
div = soup.find(id="cnblogs_post_body")
#print(div.get_text())

filename = title+'.txt'
with open(filename,'w',encoding='utf-8') as f:
  f.write(div.text)
'''