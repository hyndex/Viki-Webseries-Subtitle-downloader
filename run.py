from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.request
import time

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
driver = webdriver.Chrome(ChromeDriverManager().install())
url=input('enter the viki webseries url: ')
driver.get(url)
time.sleep(5)
driver.find_element_by_id('horizontal_tab_episodes').click()
links=[]
time.sleep(5)
tabs = driver.find_elements_by_class_name('sc-1dg0jos-0')
for tab in tabs:
    tab.click()
    time.sleep(5)
    html = driver.find_element_by_class_name('bjutxy-2')
    html = html.get_attribute('innerHTML')
    for j in range(len(html.split('"/video'))-1):
        i=j+1
        temp=html.split('"/video')[i]
        temp='https://www.viki.com/video'+temp.split('"')[0]
        links.append(temp)
        
count=0
driver.maximize_window()
for link in links:
    count=count+1
    print(count)
    driver.get('https://savesubs.com/process?url='+link)
    time.sleep(5)
    for i in driver.find_elements_by_css_selector("li"):
        if i.get_attribute('innerHTML').count('ENGLISH')>0:
            i.find_element_by_link_text('SRT').click()
    time.sleep(10)