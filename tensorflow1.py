import tensorflow as tf

basic_addition_graph = tf.Graph()
with basic_addition_graph.as_default():
    a = tf.constant([2,5,7])
    b = tf.constant([1,3,8])
    c = tf.constant([7,9,0])

    x = tf.add(a,b)
    y = tf.multiply(x,c)

#Create A session to RUN the Graph
with tf.Session(graph = basic_addition_graph) as sess:
    print(sess.run(y))

