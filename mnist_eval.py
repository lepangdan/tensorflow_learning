import time
import tensorflow as tf
import mnist_inference
import mnist_train

# 每10秒加载一次最新的模型，并在测试数据上测试最新的模型的正确率
EVAL_INTERVAL_SECS=10

def evaluate():
    # a=tf.constant([1,2])
    # # print(a.graph)
    with tf.Graph().as_default() as g:  # 新建了一个graph g， make g  default graph
        # Create ExponentialMovingAverage object
        variable_average=tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variable_to_restore=variable_average.variables_to_restore()
        print(variable_to_restore)
        print(tf.get_default_graph().get_operations())
        with tf.Session() as sess:
            print()


def main(argv=None):
    evaluate()


if __name__=="__main__":
    tf.app.run()
