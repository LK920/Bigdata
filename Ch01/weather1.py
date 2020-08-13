"""
date : 20/07/15
name : kang
content : 날씨 크롤링 실습하기

"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

# 세션시작

sess = req.session()

# 날씨데이터 요청
html = sess.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')

# 파싱
dom = bs(html.text, 'html.parser')

#지점,시정,현재기온,이슬점온도,체감온도,일강수,습도,풍향,해면기압
locals = dom.select('#content_weather > table > tbody > tr > td > a')
visibilities = dom.select('#content_weather > table > tbody > tr > td:nth-child(3)')
temps1 = dom.select('#content_weather > table > tbody > tr > td:nth-child(6)')
temps2 = dom.select('#content_weather > table > tbody > tr > td:nth-child(7)')
temps3 = dom.select('#content_weather > table > tbody > tr > td:nth-child(8)')
rains1 = dom.select('#content_weather > table > tbody > tr > td:nth-child(9)')
rains2 = dom.select('#content_weather > table > tbody > tr > td:nth-child(10)')
winds = dom.select('#content_weather > table > tbody > tr > td:nth-child(11)')

hpas = dom.select('#content_weather > table > tbody > tr > td:nth-child(13)')

#저장 디렉토리 생성
dir='/home/bigdata/weather/weather-{:%y-%m-%d}'.format(datetime.now())
if not os.path.exists(dir) :
    os.mkdir(dir)

# 파일로 저장 20-07-15-16.csv
fname = "{:%y-%m-%d-%H}.csv".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')
#csv 파일 헤더
file.write('지점,시정,현재기온,이슬점온도,체감온도,일강수,습도,풍향,해면기압\n')

for i in range(0, len(locals)):

    file.write(locals[i].text+', '+
               visibilities[i].text+', ' +
               temps1[i].text+', ' +
               temps2[i].text+ ', ' +
               temps3[i].text+ ', ' +
               rains1[i].text+ ', ' +
               rains2[i].text+ ', ' +
               winds[i].text+ ', ' +
               hpas[i].text+ "\n")

#파일닫기
file.close()

