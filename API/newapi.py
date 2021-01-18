from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask_cors import CORS
from flask import request
from flask import abort
from flask import jsonify

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/model', methods=('POST',))
def query_example():
    filepath = request.args.get('filepath') #if key doesn't exist, returns None
    webviewPath = request.args['webviewPath'] #if key doesn't exist, returns a 400, bad request error

    
    return jsonify(webviewPath)

if __name__ == '__main__':
    app.run()  # run our Flask app


