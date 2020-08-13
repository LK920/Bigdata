"""
date: 2020/07/16
name: kang
content : 파이썬 네이버 영화 리뷰평점 데이터 수집하기
"""

import os
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from pymongo import MongoClient as mongo
from datetime import datetime
import time, logging

#로거 생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

#로그 포멧 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#핸들러 생성
fileHandler = logging.FileHandler('./movie.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

# 로거 + 핸들러 연결
logger.addHandler(fileHandler)

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#browser = webdriver.Chrome('../Ch01/chromedriver.exe', chrome_options=chrome_options)
browser = webdriver.Chrome('../Ch01/chromedriver.exe')
browser.implicitly_wait(3)

logger.info('크롬 가상브라우저 실행 완료')

#랭크 페이지 번호 변수 선언
page=1

while True:

    logger.info('첫번째 while문 시작')
    #랭크 변수 선언(0~49)
    i = 0
    time.sleep(1)

    while True:
        logger.info('두번째 while문 시작')
        #네이버 영화 랭킹 평점순 이동
        browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200720&page='+str(page))
        browser.implicitly_wait(3)
        logger.info('네이버 영화 랭킹 평점순 이동')

        try:

            #네이버 영화 랭킹  클릭
            ranks = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
            ranks[i].click()
            browser.implicitly_wait(3)
            logger.info('영화 랭킹 클릭 평점순 이동 page=%d'%page)

        except:
            logger.warning('두번째 while try 예외발생')
            break

        #네이버 영화 랭킹 1위의 평점 클릭
        review_tab = browser.find_element_by_css_selector('#movieEndTabMenu > li:nth-child(5) > a')
        review_tab.click()
        browser.implicitly_wait(3)
        logger.info('영화평점탭 틀릭')

        #영화 제목
        tit_tag = browser.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')
        #href는 = 뒤에 네이버에서 부여한 코드 값
        href = tit_tag.get_attribute('href')
        a = href.rfind('=')+1

        code= href[a:]
        title = tit_tag.text
        logger.info('영화 제목: %s'%title )


        #iframe 전환 왜냐하면 네이버 프레임 속에 또다른 html인 iframe으로 걸려 있기 때문이다.
        #switch_to_frame()괄호 안에는 전환할 iframe의 name값을 넣어준다.
        browser.switch_to.frame('pointAfterListIframe')
        browser.implicitly_wait(3)
        logger.info('iframe전환' )

        #최신순 클릭
        tag_latest_a = browser.find_element_by_css_selector('#orderCheckbox > ul.sorting_list > li:nth-child(2) > a')
        tag_latest_a.click()
        browser.implicitly_wait(3)
        logger.info('최신순 전환')

        #MongoDB 접속, DB, collection 선택 (수업서버로 올릴시에는 27017/krg로 db도 설정해야한다.)
        conn = mongo('mongodb://krg:1234@192.168.100.101:27017')
        db = conn.get_database('krg')
        collection = db.get_collection('movie_review')
        logger.info('몽고DB 접속')

        #현재 페이지 설정
        page_num = 1

        while True:
            try:

                #페이지 클릭
                page_id = 'pagerTagAnchor'+str(page_num)
                page_btn = browser.find_element_by_id(page_id)
                page_btn.click()
                browser.implicitly_wait(3)
                logger.info('현재 페이지 : %d' % page_num )

            except:
                logger.info('페이지 없음' )
                break



            #평점, 리뷰, 날짜 수집
            li_tags = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')
            list_data = []

            for li in li_tags:
                score = li.find_element_by_css_selector(' .star_score > em')
                reple = li.find_element_by_css_selector(' .score_reple > p > span')
                rdate = li.find_element_by_css_selector(' .score_reple > dl > dt > em:nth-child(2)')
                list_data.append({'title ': title,
                                  'code': code,
                                  'score': score.text,
                                  'reple': reple.text,
                                  'rdate': rdate.text})

            #insert 실행
            collection.insert_many(list_data)

            print(page_num, 'insert완료...')
            page_num += 1

        #그 다음 영화 리뷰 수집을 위한 랭크 변수 증가
        print(i, 'insert2완료')
        i += 1
    page += 1







print('완료/....')
#브라우져종료
browser.close()
browser.quit()

    #cron작업 등록
    #crontab -e
    # * * * * * python3 /root/naver.py
    #(분, 시, 일, 월, 요일)
    #매분마다 python3 /root/naver.py 을 실행

    #cron데몬 서비스 시작/종료
    #systemctl start crond
    #systemctl stop crond

    #cron작업 조회
    #crentab -l

    #cron작업 삭제
    #crentab -r