"""
date : 20/08/18
name : kang
content : 텐서플로우 1.x - helloworld 실습하기
"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#텐서플로우 버전 확인
print(tf.__version__)

#그래프 생성
hello = tf.constant('hello Tensorflow')

#세션 생성
sess = tf.Session()

#그래프 실행
result = sess.run(hello)
print(result)

#세션종료
sess.close()