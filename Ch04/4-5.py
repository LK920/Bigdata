"""
date : 20/08/11
name : kang
content : 머신러닝 - 다중선형회귀 분석 연습문제
"""
from sklearn.linear_model import LinearRegression

#학습데이터
train_data = [[170, 30, 1], [155, 60, 2], [150, 50, 2], [175, 40, 1], [165, 25, 1]]
train_label = [65, 50, 45, 70, 55]


#학습하기
model = LinearRegression()
model.fit(train_data,train_label)

#모델검증
test_data = [[180, 27, 1], [157, 27, 2]]
result = model.predict(test_data)

print('result : ', result)