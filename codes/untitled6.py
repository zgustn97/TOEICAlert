from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time



options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/ADMIN/Desktop/ch_selenium/driver/chromedriver', options=options)

driver.implicitly_wait(3)

driver.get("https://exam.toeic.co.kr/receipt/centerMap.php")

find = []
date = []
time.sleep(3)

search = driver.find_element_by_css_selector('#centerName')
search.send_keys('강릉')
btn = driver.find_element_by_css_selector('#contents > div > div.top_search > div > a')
btn.click()

info = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.detail_area > ul > li:nth-child(2) > span > span > a') 
info.click()
name = driver.find_element_by_css_selector('#contents > div > div.search_list > div.default_cell.centerInfo > div.table_data > table > tbody > tr:nth-child(1) > td').text

deinfo = driver.find_element_by_css_selector('#storeExamDate').text
find=list((map(str,deinfo.split(" "))))

for cnt in range(0,len(find)):
    if cnt%2 == 0:
        date.append(find[cnt])
    elif cnt == 0:
        date.append(find[cnt])