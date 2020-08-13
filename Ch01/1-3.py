"""
date : 2020/07/13
name :  kang
content : 파이선 네이버 뉴스 파싱
"""
from bs4 import BeautifulSoup as bs
import urllib.request as req

html = req.urlopen('https://news.naver.com/').read()

dom = bs(html, 'html.parser')
news_titles = dom.select('#section_it  div > ul > li strong')

print(news_titles)

for tit in news_titles:
    print(tit.string)
