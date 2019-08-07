from selenium import webdriver
import csv
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=option)

csv_file = open("playlist.csv", "w", encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])

# 解析每一页，直到‘下一页’为空
while url != 'javascript:void(0)':
    # 用webDriver加载页面
    browser.get(url)
    # 切换到内容的iframe
    browser.switch_to_frame("contentFrame")
    # 定位歌单标签
    data = browser.find_element_by_id(
        "m-pl-container").find_elements_by_tag_name("li")
    # 解析一页中的所有歌单
    for i in range(len(data)):
        # 获取播放数
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0]) > 500:
            msk = data[i].find_element_by_css_selector("a.msk")
            writer.writerow([msk.get_attribute('title'),
                             nb, msk.get_attribute('href')])
    url = browser.find_element_by_css_selector(
        "a.zbtn.znxt").get_attribute("href")
csv_file.close()
