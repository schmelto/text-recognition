# https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

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

model.fit(train_images, train_vec_labels, epochs=10, verbose=True)

eval_loss, eval_accuracy = model.evaluate(test_images, test_vec_labels, verbose=False)
print("Model accuracy: %.2f" % eval_accuracy)

config = model.to_json()

app = Flask(__name__)
CORS(app)
api = Api(app)


class Model(Resource):
    # methods go here
    def get(self):
        return {'data': config}, 200  # return data and 200 OK code


class Model2(Resource):
    # methods go here
    def get(self):
        return {'data': eval_accuracy}, 200  # return data and 200 OK code


api.add_resource(Model, '/model')  
api.add_resource(Model2, '/model2')  

if __name__ == '__main__':
    app.run()  # run our Flask app