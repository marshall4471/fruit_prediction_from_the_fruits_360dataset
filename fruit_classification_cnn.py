# -*- coding: utf-8 -*-
"""fruit_classification_cnn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aofwv5h3BbHf_PoSantjIgg6AlbvMsCK
"""

from keras.models import Sequential

import tensorflow as tf

import keras as k

from keras import layers

from keras.layers import Conv2D

from keras.layers import Dense

from keras.layers import Flatten

from keras.layers import Dropout

from keras.layers import Activation

from keras.layers import MaxPooling2D

from keras import preprocessing

test_datagen = k.preprocessing.image.ImageDataGenerator(rescale=1./255)

from google.colab import drive
drive.mount("/content/gdrive")

file = ('/content/gdrive/MyDrive/fruits/fruits-360/Test')

file2 = ('/content/gdrive/MyDrive/fruits/fruits-360/Training')

train_datagen = k.preprocessing.image.ImageDataGenerator(rescale=1./255, horizontal_flip=True, validation_split=0.2)

train_gen = train_datagen.flow_from_directory(directory = file2, subset='training', target_size=(100,100), shuffle=True, class_mode='categorical', batch_size=500)

val_gen = train_datagen.flow_from_directory(directory= file2, subset='validation', shuffle=True, class_mode='categorical', target_size=(100,100), batch_size=500)

test_gen = test_datagen.flow_from_directory(directory=file, shuffle=True, target_size=(100,100), class_mode='categorical', batch_size=500)

from tensorflow.keras import Model

import keras



model = keras.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='relu', input_shape=(100,100,3)),
    layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu'),
    layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), activation='relu'),
    layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu'),
    layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(131, activation='softmax')
])



model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

history = model.fit(train_gen, validation_data = val_gen, batch_size=32, epochs=12)

model.save('fruit_pred.h5')

import cv2

import matplotlib.pyplot as plt

import numpy as np

from google.colab import files
uploaded = files.upload()

x = plt.imread('avocado.jpg')
plt.imshow(x)

x = x/255

x = np.resize(x,(1,100,100,3))

x.shape

classes = list(train_gen.class_indices)

print(classes[np.argmax(model.predict(x))])
