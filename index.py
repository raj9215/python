from flask import Flask, request, jsonify

app = Flask(__name__)

from src.config.database import mydb
from src.routes.routes import *

if __name__ == '__main__':
    app.run(debug=True)