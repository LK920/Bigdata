"""
date : 20/08/11
name : kang
content : 머신러닝 - 로지스틱회귀 분석 실습하기
"""

from sklearn.linear_model import LogisticRegression

#훈련데이터
train_data = [[40,30],[30,80],[20,70],[70,40],[60,20]]
train_label = [+1,-1,-1,+1,+1]

#학습하기
model = LogisticRegression()
model.fit(train_data, train_label)

#검증하기

result = model.predict(train_data)
print('result : ', result)

#새로운 데이터 검증
test_data = [[46.12, 60.53],[27.20, 45.12],[37.15, 51.22]]
test_result = model.predict(test_data)
print('result :', test_result)