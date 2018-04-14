import tensorflow as tf
import mnist_inference
import numpy as np
import gzip
import os

DATA_PATH = '/Users/pangdan/Downloads/nn_robust_attacks-master/data'
REGULARAZITION_RATE = 0.0001
LEARNING_RATE_BASE=0.8
LEARNING_RATE_DECAY=0.99
BATCH_SIZE=100
TRAINING_STEPS=50000
MOVING_AVERAGE_DECAY=0.99
MODEL_SAVE_PATH='Model'
MODEL_NAME='mnist'



def extract_data(filename, num_images):
    with gzip.open(filename) as bytestream:
        bytestream.read(16)   # 读取16个字节
        buf = bytestream.read(num_images*28*28)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = (data / 255) - 0.5
        data = data.reshape(num_images, 28*28)   # 1:one channel(grey-image)
        return data


def extract_labels(filename, num_images):
    with gzip.open(filename) as bytestream:
        bytestream.read(8)   # 读取8个字节
        buf = bytestream.read(1 * num_images)
        labels = np.frombuffer(buf, dtype=np.uint8)
    return (np.arange(10) == labels[:, None]).astype(np.float32)


train_data = extract_data('/'.join((DATA_PATH, 'train-images-idx3-ubyte.gz')), 60000)
train_labels = extract_labels('/'.join((DATA_PATH, 'train-labels-idx1-ubyte.gz')), 60000)
test_data = extract_data('/'.join((DATA_PATH, 't10k-images-idx3-ubyte.gz')), 10000)
test_labels = extract_labels('/'.join((DATA_PATH, 't10k-labels-idx1-ubyte.gz')), 10000)
# print(test_data.shape)
# train_data=train_data.reshape((:,74))

def train():
    x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUPUT_NODE], name='y-input')
    regularize= tf.contrib.layers.l2_regularizer(REGULARAZITION_RATE)
    y = mnist_inference.inference(input_tensor=x, regularizer=regularize)
    cross_entropy=tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_)  # tf.nn.softmax_cross_entropy_with_logit\
    # 放的是y_的类别。而不是one-hot 向量
    cross_entropy_mean=tf.reduce_mean(cross_entropy)
    loss=cross_entropy_mean+tf.add_n(tf.get_collection('losses'))
    global_step = tf.Variable(0, trainable=False)
    variable_averages=tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    variable_averages_op=variable_averages.apply()
    learning_rate=tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,60000/BATCH_SIZE,LEARNING_RATE_DECAY)
    train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)

    saver=tf.train.Saver()
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        if not os.path.isdir('Model'):
            os.makedirs('Model')
        for i in range(TRAINING_STEPS):
            start=(i * BATCH_SIZE)%60000
            end=min(start + BATCH_SIZE,60000)
            train_op=tf.group(train_step,variable_averages_op)
            _, loss_value,step=sess.run([train_op, loss, global_step],feed_dict={x:train_data[start:end], y_:train_labels[start:end]})
            if step % 1000==0:
                print("After %d training steps, loss on training batch is %g." %(step,loss_value))
                saver.save(sess,os.path.join(MODEL_SAVE_PATH,MODEL_NAME),global_step=global_step)


def main(argv=None):
    train()

if __name__=="__main__":
    tf.app.run()





