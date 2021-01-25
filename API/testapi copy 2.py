
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

import pathlib

data = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

train_images = train_images / 255
test_images = test_images / 255

total_classes = 10
train_vec_labels = keras.utils.to_categorical(train_labels, total_classes)
test_vec_labels = keras.utils.to_categorical(test_labels, total_classes)

model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(28, 28)),
                          keras.layers.Dense(128, activation='sigmoid'),
                          keras.layers.Dense(10, activation='sigmoid')
])

# sgd = keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(
    optimizer='sgd',
    loss='mean_squared_error',
    metrics=['accuracy'])

model.fit(train_images, train_vec_labels, epochs=2, verbose=True)

eval_loss, eval_accuracy = model.evaluate(test_images, test_vec_labels, verbose=False)
print("Model accuracy: %.2f" % eval_accuracy)

config = model.to_json()

img1 = 'C:/Users/tomsc/Downloads/img_1.jpg'

img2 = tf.keras.preprocessing.image.img_to_array(
img1, data_format=None, dtype=None
)

prediction = model.predict(img2)
print(prediction)
