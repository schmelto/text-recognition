# https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS
from flask import request
from flask import abort

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
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('filepath', required=True)  # add args
        parser.add_argument('webviewPath', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'filepath': args['filepath'],
            'webviewPath': args['webviewPath'],
        })
        return {'data': new_data}, 200  # return data with 200 OK

api.add_resource(Model, '/model')  


if __name__ == '__main__':
    app.run()  # run our Flask app