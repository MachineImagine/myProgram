# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
m1 = tf.constant([[2,2]])
m2 = tf.constant([[3],[3]])
dot_operation =tf.matmul(m1,m2)
print(dot_operation)
sess=tf.Session()
result= sess.run(dot_operation)
print(result)

hello = tf.constant([[2,2]])
sess2=tf.Session()
print(sess2.run(hello))
a= tf.constant(10)
b= tf.constant(32)
print(sess2.run(a+b))