
from selenium import webdriver
from openpyxl import Workbook, load_workbook
from datetime import datetime

browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')

item_boxs = browser.find_elements_by_css_selector("#content > div > .selection_area > .selection_content > .field_list > div > div > ul:nth-child(1) > li > .item_box")

workbook = Workbook()

sheet = workbook.active

for item in item_boxs:
    num = item.find_element_by_css_selector('.item_num').text
    title = item.find_element_by_css_selector('.item_title_wrap > .item_title').text
    now = "{:%y%m%d%H%M%S}".format(datetime.now())

    sheet.append(['%s' % num,'[%s]' % title,'%s\n' % now])

#엑셀 저장
workbook.save('./testx.xlsx')
workbook.close()

print('완료')