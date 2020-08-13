"""
date :20/07/14
name : kang
content : 파이썬 엑셀파일 데이터 출력
"""
import openpyxl

#엑셀 파일 열기
fname = './testx.xlsx'
workbook = openpyxl.load_workbook(fname)

#첫번째 시트 선택
sheet = workbook.worksheets[0]

#시트의 각행을 순서대로 출력
for row in sheet.rows:
    print('%s,%s,%s' % (row[0].value, row[1].value, row[2].value))