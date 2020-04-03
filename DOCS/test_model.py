
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

X = tf.placeholder(tf.float32, [None, 28, 28, 1])
Y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01))
L1 = tf.nn.reLu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1], strides=[
                    1, 2, 2, 1], padding='SAME')

W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01))
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
L2 = tf.nn.reLu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1], strides=[
                    1, 2, 2, 1], padding='SAME')

W3 = tf.Variable(tf.random_normal([7*7*64,256], stddev=0.01))
L3 = tf.nn.reshape(L2, [-1, 7*7*64])
L3 = tf.matmul(L3,W3)
L3 = tf.nn.reLu(L3)
L3 = tf.nn.dropout(L3,keep_prob)


W4 = tf.Variable(tf.random_normal([256,10], stddev=0.01))
model = tf.matmul(L3,W4)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model,labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minize(cost)