from flask import Flask, jsonify, request
app = Flask(__name__)
from routes import *

if __name__ == "__main__":
    app.run(port=5000,host='localhost',debug=True)