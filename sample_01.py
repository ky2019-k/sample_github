import tensorflow as tf

a = tf.constant(1,name='a')
b = tf.constant(2,name='b')

c = a + b 

with tf.Session() as sess:
    print(sess.run(c))