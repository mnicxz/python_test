import urllib.request
import re
from bs4 import BeautifulSoup

url = "https://www.cnblogs.com/xingzhui/default.html?page="
pagenum = 7


def geturl(url):
    allurls = []
    for i in range(1, pagenum+1):
        newurl = url+str(i)
        html_page = getpage(newurl)
        #url_pattern = r'<a.*class="postTitle2".*href="(.*)".*</a></div>'
        url_pattern = r'<a.*class="postTitle2" href="(.*)">'
        url_match = re.findall(url_pattern, html_page)
        for urls in url_match:
            allurls.append(urls)
    print(allurls)
    return allurls


def getpage(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    html_page = resp.read().decode("utf-8")
    return html_page


def gettitle(html_page):
    title_pattern = r'<a.*id="cb_post_title_url".*>(.*)</a>'
    # <a id="cb_post_title_url">&lt;jsp:include&gt;和&lt;%@ include %&gt;的区别</a>
    title_match = re.search(title_pattern, html_page)
    title = title_match.group(1)
    return title


def getbody(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    div = soup.find(id="cnblogs_post_body")
    return div.get_text()


urls = []
urls = geturl(url)
for newurl in urls:
    html_page = getpage(newurl)
    title = gettitle(html_page)
    print(title)
    body = getbody(html_page)
    filename = r"D:\chenchen2\My Documents\test\ "+title+".txt"
    #TODO:将目标输出到指定文件夹
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(body)

input("exit")
