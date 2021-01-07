import tensorflow as tf

a = tf.constant([2,5,7])
b = tf.constant([1,3,8])
c = tf.constant([7,9,0])

x = tf.add(a,b)
y = tf.multiply(x,c)

print(x)
print(y)