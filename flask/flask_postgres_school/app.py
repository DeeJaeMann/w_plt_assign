#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

str_app_ep = "/api/v1/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://deemann@localhost/school'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)

@app.route("/", methods=['GET'])
def display_home() :
    str_response = """
<h1>Home</h1>
<ul>
<li><a href=\"/api/v1/students/\">Get Students</a>
<li><a href=\"/api/v1/teachers/\">Get Teachers</a>
<li><a href=\"/api/v1/subjects/\">Get Subjects</a>
</ul>
"""
    return str_response

def get_this_subject(int_id) :
    qry_subjects = Subjects.query.all()

    for subject in qry_subjects :
        if subject.id == int_id :
            return subject.subject

@app.route(f"{str_app_ep}students/")
def get_students():
    qry_students = Student.query.all()

    lst_students = [
        {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'age': student.age,
            'subject': get_this_subject(student.subject)
        }
        for student in qry_students
    ]

    return jsonify(lst_students)

@app.route(f"{str_app_ep}teachers/")
def get_teachers():
    pass

@app.route(f"{str_app_ep}subjects/")
def get_subjects():
    pass


if __name__ == '__main__' :
    app.run(debug=True)