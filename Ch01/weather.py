"""
date :20/07/13
name : kang
content : 파이썬 데이터 전송 후 페이지 요청하기
"""


from selenium import webdriver
from datetime import datetime

#크롬 가상브라우저 실행
browser = webdriver.Chrome('chromedriver.exe')

#현재 날씨로 이동메인 이동
browser.get('https://www.weather.go.kr/w/weather/now.do')

#강릉 출력
city = browser.find_element_by_css_selector('#sfc-city-weather > div.cont-box02 > div > div.cont02 > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a')
temp = browser.find_element_by_css_selector('#sfc-city-weather > div.cont-box02 > div > div.cont02 > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')

print('도시 :', city.text)
print('현재기온 :', temp.text)

fname = "{:%y-%m-%d-%H-%M}".format(datetime.now())
file = open(fname, mode='w', encoding='utf-8')

file.write(city.text)
file.write(temp.text)
file.close()
"""
#파일로 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(fname, mode='w', encoding='utf-8')

file.write('순위,제목,날짜\n')
now = "{:%y%m%d%H%M%S}".format(datetime.now())

for item in item_boxs:
    file.write('%s,' % item.find_element_by_css_selector('.item_num').text)
    file.write('[%s],' % item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % now)

#파일닫기
file.close()
"""

