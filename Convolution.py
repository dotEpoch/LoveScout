# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
import os
import cv2
import imghdr
from matplotlib import pyplot as plt
import numpy as np

from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten #Dropout
## Functional Deep Learning model would be better to link the random prompts within the network


### __PREPARATION__ ###

## GPU ACCELERATION
gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
    
# tf.config.list_physical_devices("GPU")
# print(gpus)

## FILTER
data_dir = "MtlData"
extensions = ["jpeg", "jpg", "bmp", "png"]

for folders in os.listdir(data_dir):
    for images in os.listdir(os.path.join(data_dir, folders)):
        path = os.path.join(data_dir, folders, images)
        try:
            img = cv2.imread(path)
            tip = imghdr.what(path)
            if tip not in extensions:
                print("extension not allowed".format(path))
                os.remove(path)
        except Exception:
            print ("image rejected".format(path))
            
## PIPE
data = tf.keras.utils.image_dataset_from_directory("MtlData")
data_iterator = data.as_numpy_iterator()

## ARRAYS
batch = data_iterator.next()


## LEGEND
# 0
# 1 
# 2 
# 3
# 4 
# 5

### __PREPROCESSING__ ###

## NORMALIZATION
#incrementally normalize to 0 - 1 RGB values

data = data.map(lambda x, y: (x/255, y))

normal_iter = data.as_numpy_iterator()
batch = normal_iter.next()
print(batch[0].max())

## PARTITION

print(len(data))

training_size = int(len(data)*0.7)
validation_size = int(len(data)*0.2)+1
test_size = int(len(data)*0.1)

training = data.take(training_size)
validation = data.skip(training_size).take(validation_size)
test = data.skip(training_size + validation_size).take(test_size)

## possible to do some color processing
## Gamma correction / 

### __CONVOLUTION NEURAL NETWORK__ ###

model = Sequential()

model.add(Conv2D(16, (3,3), 1, activation = "relu", input_shape = (256, 256, 3)))
model.add(MaxPooling2D())

model.add(Conv2D(32, (3,3), 1, activation = "relu"))
model.add(MaxPooling2D())

model.add(Conv2D(16, (3,3), 1, activation = "relu"))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(256, activation = "relu"))
model.add(Dense(1, activation = "sigmoid"))
##Fully connected layers of neurons => dense

model.compile("adam", loss = tf.losses.BinaryCrossentropy(), metrics = ["accuracy"])
print(model.summary())
#Pretty good

### __TRAINING__ ###

logs = "Logs"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir = logs)
hist = model.fit(training, epochs = 10, validation_data = validation, callbacks = [tensorboard_callback])


### __PERFORMANCE__ ###


fig = plt.figure()
plt.plot(hist.history["loss"], color = "red", label = "Loss")
plt.plot(hist.history["val_loss"], color = "orange", label = "Validation Loss")
plt.plot(hist.history["accuracy"], color = "lime", label = "accuracy")
plt.plot(hist.history["val_accuracy"], color = "lime", label = "validation accuracy")
fig.suptitle("Loss and Accuracy", fontsize = 20)
plt.legend(loc = "upper left")
plt.show()







