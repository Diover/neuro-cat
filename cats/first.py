import tensorflow as tf

def test_tensorboard():
  a = tf.constant(5)
  b = tf.constant(4)
  c = a+b
  with tf.Session() as sess:
    Writer = tf.summary.FileWriter("../../log", sess.graph)
    Writer.close()

def hello_world():
  hello = tf.constant('Hello, TensorFlow!')
  sess = tf.Session()
  print(sess.run(hello))

hello_world()
test_tensorboard()