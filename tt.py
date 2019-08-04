import urllib.request
import re

def get_page(url):
    res = urllib.request.urlopen(url)
    page = res.read().decode('utf-8', 'ignore')
    return page

def get_url(url):
    total_url = []
    page = get_page(url)
    url_pattern = r'<td class="L"><a href="(.*)">.*</a>'
    url_match = re.findall(url_pattern, page)
    for url in url_match:
        total_url.append(url)
    return url

url = 'https://www.23us.so/files/article/html/3/3574/index.html'
urls = get_url(url)
print(get_page(url))
print(urls)
