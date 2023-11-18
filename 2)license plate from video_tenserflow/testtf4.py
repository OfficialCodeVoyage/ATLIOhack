import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU available")
else:
    print("GPU not available")
