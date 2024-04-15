import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')

print("=============================================================")
print("Tensorflow version: " + tf.__version__)
for gpu in gpus:
    print("Name:", gpu.name, " Type:", gpu.device_type)
print("=============================================================")
