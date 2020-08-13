"""
date: 2020/07/22
name: kang
content : 날씨 클로링을 하루마다 로컬서버에서 hdfs로 옮기기 실습하기
"""

from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop
from datetime import datetime
#하둡 접속
hdfs = hadoop(host='192.168.100.101', port= '50070', user_name='root')
#로컬 /home/bigdata/naver/naver-20-xx-xx-xx 를 하둡 /naver/ 복사

month = datetime.today().month
day = datetime.today().day-1
if(month<10):
    month = '0'+str(month)
if(day<10):
    day = '0'+str(day)
t = str(month)+'-'+str(day)

print(t)

hdfs.make_dir('/naver')



#로컬의 /home/bigdata/naver/naver-20-xx-xx-xx를 삭제
hdfs.delete_file_dir('/home/bigdata/naver/naver-20-'+t,)