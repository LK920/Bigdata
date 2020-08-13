"""
date : 20/08/12
name : kang
content : 머신러닝 - mnist 숫자이미지  SVM 분석 실습하기
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
#데이터 프레임 생성
df_mnist_train  = pd.read_csv('./data/mnist_train.csv')
df_mnist_test   = pd.read_csv('./data/mnist_test.csv')
df_mnist_test
#데이터 프레임 생성
df_mnist_train  = pd.read_csv('./data/mnist_train.csv')
df_mnist_test   = pd.read_csv('./data/mnist_test.csv')

#학습데이터 준비 및 데이터 초기화
df_mnist_train_data =  df_mnist_train.iloc[:,1:]/255 #0에서1 사이 실수가 됨.
df_mnist_train_label = df_mnist_train.iloc[:,0]

#테스트데이터 준비 및 데이터 초기화
df_mnist_test_data =  df_mnist_test.iloc[:,1:]/255 #0에서1 사이 실수가 됨.
df_mnist_test_label = df_mnist_test.iloc[:,0]

#학습하기
model = svm.SVC()
model.fit(df_mnist_train_data, df_mnist_train_label)

#검증하기
result = model.predict(df_mnist_test_data)

#학습률 확인

score = metrics.accuracy_score(df_mnist_test_label, result)
print(score)