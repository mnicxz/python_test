from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://www.cnblogs.com/yahutiaotiao/p/8044849.html'

browser=webdriver.Chrome()
browser.get(url)
browser.find_element_by_css_selector()