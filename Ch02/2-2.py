"""
date: 2020/07/16
name: kang
content : 파이썬 mongodb find 실습하기
"""
from pymongo import MongoClient as mongo
#mongodb 접속

conn = mongo('mongodb://krg:1234@192.168.100.101:27017')

#db선택
db = conn.get_database('krg')

#collection 선택
collection = db.get_collection('member')

#select * from 'memeber'
rs = collection.find()

for row in rs:
    print('%s, %s' % (row['uid'], row['name']))

#selcet * from 'member' where uid='a101'
rs2 = collection.find({'uid':'a101'})

for row in rs2:
    print('%s, %s, %s' % (row['uid'],row['name'],row['hp']))

#select* from 'member' where uid ='A101' and name='김유신'
rs3 = collection.find({'uid':'A101','name':'김유신'})
for row in rs3:
    print('%s, %s, %s, %s' % (row['uid'],row['name'],row['hp'],row['pos']))

#select * from 'member' where dep > 103
rs4 = collection.find({'dep':{'$gt':103}})
for row in rs4:
    print('%s, %s, %s, %s, %d' % (row['uid'],row['name'],row['hp'],row['pos'],row['dep']))
