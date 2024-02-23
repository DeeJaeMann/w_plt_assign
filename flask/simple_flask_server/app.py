#!/usr/bin/env python3
# This Flask api retrieves data from the Students object and outputs the requested data
# This does not use SQL

from resources.classes.students import Students
from flask import Flask, jsonify

str_api_base = "/api/v1/"

app = Flask(__name__)
all_students = Students()

Students.load_students(Students.lst_students_raw)

@app.route('/')
def home():
    # generate a nice home page to access all end points
    str_response =  """
Hello <a href=\"/\">World</a><br>
<a href=\"/api/v1/students/\">All Students</a><br>
<a href=\"/api/v1/old_students/\">Old Students</a><br>
<a href=\"/api/v1/young_students/\">Young Students</a><br>
<a href=\"/api/v1/advance_students/\">Advance Students</a><br>
<a href=\"/api/v1/student_names/\">Student Names</a><br>
<a href=\"/api/v1/student_ages/\">Student Ages</a>
"""
    return str_response

@app.route(f"{str_api_base}students/", methods=['GET'])
def get_all_students():
    # get all students from object list
    student_list = [
        {'id': student._id, 'first_name': student._first_name, 'last_name': student._last_name, 'age': student._age, 'grade': student._grade} 
                    for student in Students.students
                    ]
    return jsonify(student_list)

@app.route(f"{str_api_base}old_students/", methods=['GET'])
def get_old_students():
    # get students older than 20 from object list
    lst_old_students = []

    for student in Students.students :
        if int(student._age) > 20 :
            lst_old_students.append(student)
    student_list = [
        {'id': student._id, 'first_name': student._first_name, 'last_name': student._last_name, 'age': student._age, 'grade': student._grade} 
                    for student in lst_old_students
                    ]
    return jsonify(student_list)
   

@app.route(f"{str_api_base}young_students/", methods=['GET'])
def get_young_students():
    # get students younger than 21 from object list
    lst_young_students = []

    for student in Students.students :
        if int(student._age) < 21 :
            lst_young_students.append(student)
    student_list = [
        {'id': student._id, 'first_name': student._first_name, 'last_name': student._last_name, 'age': student._age, 'grade': student._grade} 
                    for student in lst_young_students
                    ]
    return jsonify(student_list)


@app.route(f"{str_api_base}advance_students/", methods=['GET'])
def get_advance_students():
    # get students with grade 'A' from object list
    lst_advance_students = []

    for student in Students.students :
        if student._grade == 'A' :
            lst_advance_students.append(student)
    student_list = [
        {'id': student._id, 'first_name': student._first_name, 'last_name': student._last_name, 'age': student._age, 'grade': student._grade} 
                    for student in lst_advance_students
                    ]
    return jsonify(student_list)    


@app.route(f"{str_api_base}student_names/", methods=['GET'])
def get_student_names():
    # get only student names from object list
    student_list = [
        {'first_name': student._first_name, 'last_name': student._last_name} 
                    for student in Students.students
                    ]
    return jsonify(student_list)

@app.route(f"{str_api_base}student_ages/", methods=['GET'])
def get_student_ages():
    # get students names (join first and last) and ages
    student_list = [
        {'student_name': student._first_name + " " + student._last_name, 'age': student._age} 
                    for student in Students.students
                    ]
    return jsonify(student_list)
    
if __name__ == '__main__' :
    app.run(debug=True)