#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

str_app_ep = "/api/v1/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://deemann@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

@app.route("/", methods=['GET'])
def display_home() :
    str_response = """
<a href=\"/api/v1/students/\">Get Students</a>
"""
    return str_response

@app.route(f"{str_app_ep}students/", methods=['GET'])
def get_students():
    qry_students = Student.query.all()

    lst_students = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in qry_students
    ]

    return jsonify(lst_students)

if __name__ == '__main__':
    app.run(debug=True)