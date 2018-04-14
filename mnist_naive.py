# import tensorflow as tf


# #parameter of network architecture
# IUPUT_NODE=784
# OUTPUT_NODE=10
# LAYER1_NODE=500

#
#
# weights=tf.get_variable('Hweights',shape=[1,2],initializer=tf.truncated_normal_initializer(stddev=0.1))
# sess=tf.Session()
# sess.run(tf.initialize_all_variables())
# print(sess.run('Hweights'))

# a=tf.constant(30.0,name='a1')
# g=tf.Graph()
# with g.as_default():
#     c=tf.constant(30.0,name='c1')
#     d=tf.constant(30.0,name='c2')
#     e=c*d
#     f=tf.divide(c,d,name='divi')
# e=tf.constant(40.0,name='e')
# print (a.graph is g)
# #False
# print(e.graph is g)
# #False
# print(a.graph is tf.get_default_graph())
# #True
# print(g is tf.get_default_graph())
# #False

# Conclusion g.as_default 操作并不是把g设置成默认的计算图，而是创建一个新的计算图

# print(a.graph)
# print(g.get_operations())
# 所有的常量和计算的操作都是OP


#     a_1=tf.Variable(40.0,dtype=tf.float32,name='a1')
#     # print(g.get_operations())
#     # print(g.get_operation_by_name('divi'))
# # print(a.op)
#     opf=f.op
#     # print(opf.node_def)
#     print(opf.inputs)
#     print(opf.outputs)

# node refer to OP, 后面的name指OP的name
# node refers to OP and edge refers to tensor


# GRAPH
# OP 可以简单理解为一个个小份的特定任务，通过并发地执行Kernel实现。 每个OP 会根据当前的设备类型选择合适的Kernel实现
# A graph contain a set of tf.Operation objects, which represent units of computation; \
# and tf.Tensor objects, which represent the unit of data the flow between operations.

# A graph instance supports an arbitrary number of "collections" that are identified by name.

# -----------------------------------------------------
# 看看tf.train.Optimizer.minimize 输出的是什么？
import tensorflow as tf
import numpy as np

BATCH_SIZE = 8
STEP = 500

# construct computing graph
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1), name='hahaw1')
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

a = tf.matmul(x, w1, name='a')
y = tf.matmul(a, w2, name='y')

cross_entropy = -tf.reduce_mean(y_*tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_step = tf.train.AdadeltaOptimizer(0.01).minimize(cross_entropy)

# generate data for training

dataset_size = 128
X = np.random.rand(dataset_size, 2)
print(X[1:3, :])

Y = [[int((x1+x2) < 1)] for (x1, x2) in X]
print('hhaha', type(Y))

# train
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()   # dont have output tensor
    # print(init_op.inputs)
    # #init_op is OP
    # print(y.outputs)
    # #y is tensor
    # 为什么有时候是OP 有时候是tensor呢？
    sess.run(init_op)
    for step in range(STEP):
        start = (step * BATCH_SIZE) % dataset_size
        end = min(start + BATCH_SIZE, dataset_size)
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})

        if step % 100 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X[start:end], y_: Y[start:end]})
            print('After %i step, cross_entropy is %g', (step, total_cross_entropy))

    print(sess.run(w1))


