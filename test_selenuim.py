from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

'''#启动Chrome浏览器
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
'''

chrome_options=webdriver.ChromeOptions()
#使用 headless
#chrome_options.add_argument('--headless')#增加无界面选项
#chrome_options.add_argument('--disable-gpu')#如果不加这个选项，有时定位会出问题
#添加个人配置,unicodeescape
#chrome_options.add_argument('--user-data-dir=C:\Users\chenchen2\AppData\Local\Google\Chrome\User Data\Default')
#启动浏览器，获取源代码
#browser=webdriver.Chrome(chrome_options=chrome_options)
browser=webdriver.Chrome()
bilibili="https://www.bilibili.com/"
baidu="https://www.baidu.com/"
#browser.get(baidu)
#print(f"browser text = {browser.page_source}")
html=browser.page_source
'''
with open("sele.txt","w",encoding='utf-8') as f:
    f.write(html)
'''
#browser.find_element_by_class_name("search-keyboard").send_keys("sele")
#browser.find_element_by_tag_name("input").send_keys("selenium")
#browser.find_element_by_tag_name("input").send_keys("selenium")
#browser.find_element_by_id("su").click()
#browser.find_element_by_class_name("search-submit").click()
'''
input_first = browser.find_element_by_id("kw")
#input_second = browser.find_element_by_css_selector("#q")
#input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
#print(input_second)
#print(input_third)
input_first.send_keys("selenium")
time.sleep(1)
input_first.clear()
input_first.send_keys("python")
#browser.find_element_by_id("su").click()
'''
'''
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
#actions = ActionChains(browser)
#actions.drag_and_drop(source, target)
#actions.perform()
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

'''
url = 'https://www.zhihu.com/explore'
browser.get(url)
#browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#browser.execute_script('alert("To Bottom")')
#logo = browser.find_element_by_id('zh-top-link-logo')
#print(logo)
#print(logo.get_attribute('class'))
#input = browser.find_element_by_class_name('zu-top-add-question')
#print(input.text)
#print(input.id)
#print(input.location)
#print(input.tag_name)
#print(input.size)
print(browser.get_cookies())

#browser.back()
#time.sleep(1)
#browser.forward()
time.sleep(10)
browser.quit()


    