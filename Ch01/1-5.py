"""
date :20/07/13
name : kang
content : 파이썬 가상 웹브라우저 실습하기
(selenium(가상브러우저 제어)/크롬드라이버(가상웹브라우저) 설치)
"""
from selenium import webdriver

#크롬 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#네이버 이동
browser.get('https://www.naver.com/')

#로그인 버튼 클릭
login_btn = browser.find_element_by_css_selector('#account > a')
login_btn.click()

#아이디 비번 입력
input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')

input_id.send_keys('k01170')
input_pw.send_keys('*********')

#로그인 클릭
btn_submit = browser.find_element_by_css_selector('#log\.login')
btn_submit.click()




