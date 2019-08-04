import urllib.request
import re
from bs4 import BeautifulSoup

#url = "https://www.cnblogs.com/xingzhui/p/7881262.html"
url = 'https://maoyan.com/board/4?offset=0'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html_page = resp.read().decode("utf-8")
print(html_page)
'''
title_pattern = r'<a.*id="cb_post_title_url".*>(.*)</a>'
title_match = re.search(title_pattern, html_page)
title = title_match.group(1)
'''
# print(title)
'''
soup = BeautifulSoup(html_page, 'html.parser')
div = soup.find(id="cnblogs_post_body")
print(div.get_text())

filename = title+'.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(div.text)
    print("done")
'''