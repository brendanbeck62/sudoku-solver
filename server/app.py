import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv(dotenv_path='../.env')

# configuration
PORT = os.environ.get('FLASK_PORT') or 5000

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def home():
  return jsonify('hello world!')

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

@app.route('/board', methods=['GET'])
def board():
  response_object = {'status': 'success'}
  response_object['board'] = [
    [0,0,5,3,6,0,4,0,0],
    [9,6,2,0,0,4,0,7,0],
    [3,0,4,0,2,9,0,6,0],
    [8,2,0,9,4,0,0,1,3],
    [0,4,9,0,3,0,0,5,7],
    [0,0,0,2,0,0,9,8,0],
    [4,0,6,0,0,1,0,0,2],
    [0,0,0,6,9,3,0,0,5],
    [0,0,3,0,8,0,0,0,0]]
  return jsonify(response_object)

if __name__ == '__main__':
  app.run(port=PORT)