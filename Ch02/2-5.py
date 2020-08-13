"""
date: 2020/07/23
name: kang
content : 로깅 기본 실습하기
"""

import logging

#기본 로그레벨 설정
logging.basicConfig(filename='./2-5.log', level=logging.DEBUG)
#- 로깅 인포 부터 출력하게 만듦 즉, level=를 통해 해당 기본 로그레벨 설정가능
#filename 을 통해 로그파일 출력가능

#각 로그 레벨 기본출력
logging.debug('log debug....')
logging.info('log info.....')
#파이선에선 기본으로  warning error fatal 만 출력
logging.warning('log warn....')
logging.error('log error')
logging.fatal('log fatal....')

print('로그파일 생성완료')
