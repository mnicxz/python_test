import urllib.request
import re
from bs4 import BeautifulSoup

#url = 'https://www.23us.so/files/article/html/14/14776/7724767.html'
url = 'https://www.23us.so/files/article/html/3/3574/index.html'


def get_page(url):
    res = urllib.request.urlopen(url)
    page = res.read().decode('utf-8', 'ignore')
    return page
#print(get_page(url))


def get_url(url):
    total_url = []
    page = get_page(url)
    url_pattern = r'<td class="L"><a href="(.*)">.*</a></td>'
    url_match = re.findall(url_pattern, page)
    for url in url_match:
        total_url.append(url)
    return url


def get_novel(url):
    page = get_page(url)
    novel_pattern = r'<a href=".*">(.*)</a></dt>'
    novel_match = re.search(novel_pattern, page)
    novel = novel_match.group(1)
    return novel
#print(get_novel(url))

def get_content(url):
    page = get_page(url)
    chapter_pattern = r'<dd><h1>(.*)</h1></dd>'
    chapter_match = re.search(chapter_pattern, page)
    chapter = chapter_match.group(1)
    # return chapter
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find(id="contents")
    # return div
    d = {'chapter': chapter, 'content': div.text}
    return d


#filename = get_novel(url)+'.txt'
urls = get_url(url)
print(urls)
'''
for newurl in urls:
    d = get_content(newurl)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(d['chapter']+'\n')
        f.write(d['content']+'\n')
        # f.close()
'''
print('success')
