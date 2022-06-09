
import tensorflow as tf

load_model = tf.keras.models.load_model('pets.h5')
load_model.summary()