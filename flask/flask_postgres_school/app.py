#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

str_app_ep = "/api/v1/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://deemann@localhost/school'

db = SQLAlchemy(app)





if __name__ == '__main__' :
    app.run(debug=True)