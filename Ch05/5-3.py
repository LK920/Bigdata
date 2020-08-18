"""
date : 20/08/18
name : kang
content : 텐서플로우 자료형 실습하기
"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#그래프 생성
var1 = tf.Variable(1)
var2 = tf.Variable(2, name='var2')
var3 = tf.constant(3)
var4 = tf.constant(4, name='var4')
#placeholder는 그래프가 실행될 때 데이터를 입력하는 동적 변수
var5 = tf.placeholder(tf.int32, name='var5')
var6 = tf.placeholder(tf.int32, name='var6')

operater = (var1 + var2) * (var3+var4) * (var5+var6)

#세션 생성
sess = tf.Session()

#그래프 실행(변수 초기화 및 placeholder 데이터 입력)
sess.run(tf.global_variables_initializer())
result = sess.run(operater, feed_dict={var5: 5, var6: 6})

print(result)

#텐서플로우 그래프 시각화(텐서보드)
tf.summary.FileWriter('log5-3', graph=sess.graph)

#세션 종료
sess.close()

