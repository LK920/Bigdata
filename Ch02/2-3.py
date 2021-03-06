"""
date: 2020/07/22
name: kang
content : 파이썬 hadoop 실습하기
"""
from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop

#하둡접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

#HDFS  디렉터리 생성
hdfs.make_dir('/sample')

#HDFS 파일생성
text = 'Hello Hadoop! 반갑습니다.'
hdfs.create_file('/sample/test.txt', text.encode('utf-8'), overwrite='true')

print('프로그램 종료....')

