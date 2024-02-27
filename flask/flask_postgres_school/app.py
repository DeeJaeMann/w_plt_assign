#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Default endpoint prefix
str_app_ep = "/api/v1/"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://deemann@localhost/school'

db = SQLAlchemy(app)

# DB objects

class Student(db.Model):
    """ For student table queries
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Teachers(db.Model):
    """ For teachers table queries
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Subjects(db.Model):
    """ For subjects table queries
    """
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)

# Helper functions

def get_this_subject(int_id) :
    """Queries the subjects table given a subject ID and returns the string of the subject
    """
    # This only selects the record that has a matching id to int_id
    qry_subject = Subjects.query.filter_by(id = int_id)

    # Create a list from the query
    lst_subject = [this_subject.subject for this_subject in qry_subject]
    # Return the first element of the list
    return lst_subject[0]

def get_this_teacher(int_id) :
    """Queries the teachers table given a subject ID and returns the first and last name of the teacher
    """
    # This only selects the record that has a matching subject id to int_id
    qry_teacher = Teachers.query.filter_by(subject = int_id)

    # Create a list from the query, joining the first and last name fields
    lst_teacher = [f"{this_teacher.first_name} {this_teacher.last_name}" for this_teacher in qry_teacher]

    # Return the first element of the list
    return lst_teacher[0]

def get_these_students(int_id) :
    """Queries the students table given a subject ID and returns a list of student first and last names
    """
    # This only selects the records that have matching subject ids to int_id
    qry_students = Student.query.filter_by(subject = int_id)

    # Creates a list from the query, joining the first and last name fields
    lst_students = [f"{this_student.first_name} {this_student.last_name}" for this_student in qry_students]

    # Return the list of students
    return lst_students

# End points

@app.route("/", methods=['GET'])
def display_home() :
    """Generates a 'pretty' home page of endpoint links for testing to see the data returned
    """
    str_response = """
<h1>Home</h1>
<ul>
<li><a href=\"/api/v1/students/\">Get Students</a>
<li><a href=\"/api/v1/teachers/\">Get Teachers</a>
<li><a href=\"/api/v1/subjects/\">Get Subjects</a>
</ul>
"""
    return str_response

@app.route(f"{str_app_ep}students/", methods=['GET'])
def get_students():
    """Queries the students table and returns all student records
    """
    qry_students = Student.query.all()

    # Create a list from each record field
    # uses get_this_subject to perform a query to retrieve the subject name from the subject.id
    # uses get_this_teacher to perform a query to retrieve the teacher name from the subject.id
    lst_students = [
        {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'age': student.age,
            'class': {
                'subject': get_this_subject(student.subject),
                'teacher': get_this_teacher(student.subject)
            }
        }
        for student in qry_students
    ]

    # Return the formatted dictionary of student records
    return jsonify(lst_students)

@app.route(f"{str_app_ep}teachers/", methods=['GET'])
def get_teachers():
    """Queries the teachers table and returns all teacher records
    """
    qry_teachers = Teachers.query.all()

    # Create a list from each record field
    # uses get_this_subject to perform a query to retrieve the subject name from the subject.id
    # uses get_these_students to perform a query to retrieve the list of students from the subject.id
    lst_teachers = [
        {
            'id': teacher.id,
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'age': teacher.age,
            'class': {
                'subject': get_this_subject(teacher.subject),
                'students': get_these_students(teacher.subject)
            }
        }
        for teacher in qry_teachers
    ]

    # Return the formatted dictionary of teacher records
    return jsonify(lst_teachers)

@app.route(f"{str_app_ep}subjects/", methods=['GET'])
def get_subjects():
    """Queries the subjects table and returns the subject record, matching teacher from teacher.subject and a list of students from student.subject
    """
    qry_subjects = Subjects.query.all()

    # Create a list from each record field
    # uses get_this_teacher to perform a query to retrieve the teacher record from the subject.id ~ teacher.subject
    # uses get_these_students to perform a query to retrieve the list of student records from subject.id ~ student.subject
    lst_subjects = [
        {
            'id': subject.id,
            'subject': subject.subject,
            'teacher': get_this_teacher(subject.id),
            'students' : get_these_students(subject.id)
        }
        for subject in qry_subjects
    ]

    # Return the formatted dictionary of subject records
    return jsonify(lst_subjects)


if __name__ == '__main__' :
    app.run(debug=True)