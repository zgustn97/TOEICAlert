from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time


# def webcon(X):
#     options = Options()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome('C:/Users/ADMIN/Desktop/ch_selenium/driver/chromedriver', options=options)
    
#     driver.implicitly_wait(3)
    
#     driver.get("https://exam.toeic.co.kr/receipt/centerMap.php")
    
#     find = []
#     date = []
#     time.sleep(3)
    
#     search = driver.find_element_by_css_selector('#centerName')
#     search.send_keys(X)
#     btn = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.hall_cate_01 > ul')
#     btn.click()
    
#     info = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.detail_area > ul').text
#     print(info)
#     # info_list = list(map(set, info.split("")))
#     # print(info_list)
#     # info.click()
#     name = driver.find_element_by_css_selector('#contents > div > div.search_list > div.default_cell.centerInfo > div.table_data > table > tbody > tr:nth-child(1) > td').text
    
#     deinfo = driver.find_element_by_css_selector('#storeExamDate').text
#     find=list((map(str,deinfo.split(" "))))
    
#     for cnt in range(0,len(find)):
#         if cnt%2 == 0:
#             date.append(find[cnt])
#         elif cnt == 0:
#             date.append(find[cnt])
#     how_many = len(date)
#     return date,name,how_many





def noser(list_number):   
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome('C:/Users/ADMIN/Desktop/ch_selenium/driver/chromedriver', options=options)
    
    driver.implicitly_wait(3)
    
    driver.get("https://exam.toeic.co.kr/receipt/centerMap.php")
    
    find = []
    date = []
    time.sleep(3)
    
    # search = driver.find_element_by_css_selector('#centerName')
    # search.send_keys(X)
    # btn = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.hall_cate_01 > ul')
    # btn.click()
    # number = 1
    number = list_number
    
    info = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.hall_cate_01 > ul > li:nth-child({}) > a').format(number+1))
    # print(info)
    # info_list = list(map(set, info.split("")))
    # print(info_list)
    info.click()
    # info = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.hall_cate_01 > ul > li:nth-child({}) > a').format(number+1))
    info_text = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.hall_cate_02').text
    info_list = list(map(str, info_text.split("\n")))
    # info.click()
    print(info_list)
    return info_list
    ##########
# def noser_2(list_number[1]):
    # number = 1
    # number = list_number
    # info = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.hall_cate_02 > ul > li:nth-child({}) > a').format(number))
    # info_text = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.hall_cate_02 > ul').text
    # info_list = list(map(str, info_text.split("\n")))
    # info.click()
    # print(info_list)
    # return info_list
#%%
# def noser_3(list_number):
def noser_2(list_number):   
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome('C:/Users/ADMIN/Desktop/ch_selenium/driver/chromedriver', options=options)
    
    driver.implicitly_wait(3)
    
    driver.get("https://exam.toeic.co.kr/receipt/centerMap.php")
    
    find = []
    date = []
    time.sleep(3)
    
    # search = driver.find_element_by_css_selector('#centerName')
    # search.send_keys(X)
    # btn = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.hall_cate_01 > ul')
    # btn.click()
    # number = 1
    list_number = 1
    number = list_number
    info = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.hall_cate_01 > ul > li:nth-child({}) > a').format(number+1))
    # print(info)
    # info_list = list(map(set, info.split("")))
    # print(info_list)
    info.click()
    ##########
# def noser_2(list_number[1]):
    # number = 1
    number = list_number
    info = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.hall_cate_02 > ul > li:nth-child({}) > a').format(number))
    info_text = driver.find_element_by_css_selector('#contents > div > div.search_list > div.exam_hall > div.hall_cate_02 > ul').text
    info_list = list(map(str, info_text.split("\n")))
    info.click()    
    
    
    number = in_number
    
    info_2 = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.detail_area > ul > li:nth-child({}) > span > span > a').format(in_number))
    info_2 = driver.find_element_by_css_selector(('#contents > div > div.search_list > div.exam_hall > div.detail_area > ul').format(in_number)).text
    info_2.click()
    
    name = driver.find_element_by_css_selector(("#contents > div > div.search_list > div.default_cell.centerInfo > div.table_data > table > tbody > tr:nth-child({}) > td").format(inin_number)).text
    while True:
        try:
            info = driver.find_element_by_css_selector("#storeExamDate").text
            find=list((map(str,info.split(" "))))
            for cnt in range(0,len(find)):
                if cnt%2 == 0:
                    date.append(find[cnt])
                elif cnt == 0:
                    date.append(find[cnt])
            break
        
    
        except:
            print("시험 가능한 고사장이 없습니다.")
            break
    how_many = len(date)
    return name,date,how_many
        # name = driver.find_element_by_css_selector('#contents > div > div.search_list > div.default_cell.centerInfo > div.table_data > table > tbody > tr:nth-child(1) > td').text
        
    #     deinfo = driver.find_element_by_css_selector('#storeExamDate').text
    #     find=list((map(str,deinfo.split(" "))))
        
    #     for cnt in range(0,len(find)):
    #         if cnt%2 == 0:
    #             date.append(find[cnt])
    #         elif cnt == 0:
    #             date.append(find[cnt])
    #     how_many = len(date)
    #     return date,name,how_many
    
    
    
    # date,name,how_many = noser()
    
    # print(date,name,how_many)