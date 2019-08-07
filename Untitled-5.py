import requests
#TODO:找反爬虫图片实验
url='http://i0.hdslb.com/bfs/archive/e5439fc08ca45b79647155790acfbc2c4cd43cb6.jpg'
pic=requests.get(url).content
pic_name=url.split(r'/')[-1]
with open (pic_name,'wb') as f:
    f.write(pic)