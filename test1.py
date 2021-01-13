import sys
import numpy as np
import tensorflow as tf
from datetime import datetime
 
 
random_matrix = np.random.rand(10000,10000)
with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as session:
    with tf.device("/gpu:0"):
        
        dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
        sum_operation = tf.reduce_sum(dot_operation)
    
        startTime = datetime.now()
        result = session.run(sum_operation)
        print(result)
 
print("\n" * 2)
print("GpuTime taken:", datetime.now() - startTime)
print("\n" * 2)

with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as session:
    with tf.device("/cpu:0"):
        
        dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
        sum_operation = tf.reduce_sum(dot_operation)
    
        startTime = datetime.now()
        result = session.run(sum_operation)
        print(result)
 
print("\n" * 2)
print("CpuTime taken:", datetime.now() - startTime)
print("\n" * 2)