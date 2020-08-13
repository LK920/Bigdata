"""
date : 20/08/11
name : kang
content : 머신러닝 - SVM 분석 실습하기
"""
from sklearn import svm
from sklearn.linear_model import LogisticRegression
#학습데이터
train_data = [[0,0],[0,1],[1,0],[1,1]]
train_label = [0, 1, 1, 0]
#학습하기
svm_model = svm.SVC()
svm_model.fit(train_data,train_label)

Logic_model = LogisticRegression()
Logic_model.fit(train_data,train_label)

#모델검증
svm_result = svm_model.predict(train_data)
Logic_result = Logic_model.predict(train_data)

print('svm :', svm_result)
print('logic : ', Logic_result)


