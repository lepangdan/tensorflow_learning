# construct graph
import tensorflow as tf

# relevant parameter of network
INPUT_NODE = 784
OUPUT_NODE = 10
LAYER1_NODE = 500


def get_weight_variable(shape, regularizer):
    weights = tf.Variable(tf.truncated_normal(stddev=0.1,shape=shape),name='weights')
    if regularizer is not None:
        tf.add_to_collection('losses', regularizer(weights))
    return weights


def inference(input_tensor, regularizer):
    with tf.name_scope('layer1'):
        weight1 = get_weight_variable(shape=[INPUT_NODE, LAYER1_NODE], regularizer=regularizer)
        biases1 = get_weight_variable(shape=[LAYER1_NODE], regularizer=regularizer)
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weight1) + biases1)

    with tf.name_scope('layer2'):
        weight2 = get_weight_variable(shape=[LAYER1_NODE, OUPUT_NODE], regularizer=regularizer)
        biases2 = get_weight_variable(shape=[OUPUT_NODE], regularizer=regularizer)
        layer2 = tf.nn.relu(tf.matmul(layer1, weight2) + biases2)
    return layer2
