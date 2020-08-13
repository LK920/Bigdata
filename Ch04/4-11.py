"""
date : 20/08/12
name : kang
content : 머신러닝 - Random Forest 실습하기
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm, metrics, model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#붓꽃 데이터프레임 생성
df_pima = pd.read_csv('./data/pima-indians-diabetes.csv')

#학습데이터준비
pima_data   = df_pima.iloc[:, 0:8]
pima_label  = df_pima.iloc[:, 8]

#훈련데이터와 테스트데이터 분류
train_data, test_data, train_label, test_label = train_test_split(pima_data, pima_label)
#학습하기
rf_model = RandomForestClassifier()
svm_model = svm.SVC()

rf_model.fit(train_data, train_label)
svm_model.fit(train_data, train_label)

#검증하기
rf_result = rf_model.predict(test_data)
svm_result = svm_model.predict(test_data)

#학습률 확인
rf_score = metrics.accuracy_score(rf_result, test_label)
svm_score  = metrics.accuracy_score(svm_result, test_label)

print('rf_score :' , rf_score)
print('svm_score :' , svm_score)