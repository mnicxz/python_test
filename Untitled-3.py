import pdfkit
#FIXME:未安装whtmltopdf模块
url = "https://www.cnblogs.com/xingzhui/p/7881262.html"

pdfkit.from_url(url,'out.pdf')

print("exit")