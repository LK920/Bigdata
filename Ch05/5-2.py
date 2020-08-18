"""
date : 20/08/18
name : kang
content : 텐서플로우 1.x 그래프 실습하기
"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#그래프 생성
a = tf.Variable(1, name='a')
b = tf.Variable(2, name='b')

c= a+b

#세션생성
sess = tf.Session()

#그래프 변수 초기화
sess.run(tf.global_variables_initializer())

#그래프 실행
result = sess.run(c)
print(result)

#텐서플로우 그래프 시각화(텐서보드)
tf.summary.FileWriter('log5-2', graph=sess.graph)

#세션 종료
sess.close()

#터미널로 가서 cd Ch05로 들어간다 이후 tensrboard --logdir=./log5-2 를 실행