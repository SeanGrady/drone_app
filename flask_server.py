from flask import Flask, Response, session, jsonify
from flask_cors import CORS
from utils import establish_database_connection


app = Flask(__name__)

engine, Session = establish_database_connection('drone_webapp_testing')

@app.route('/')
def home():
    response = jsonify('drone is waiting')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/launch', methods=['GET'])
def launch():
    response = jsonify('launching drone')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/land', methods=['GET'])
def land():
    response = jsonify('landing drone')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/status', methods=['GET'])
def status():
    response = jsonify('drone is doing whatever you told it to do last :)')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

