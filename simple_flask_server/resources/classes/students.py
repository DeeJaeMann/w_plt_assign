#!/usr/bin/env python3
class Students :

    students = []

    lst_students_raw = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]

    @classmethod
    def load_students(cls, list) :

        for element in list :
            Students(**element)

        

    def __init__(self, id=None, first_name=None, last_name=None, age=None, grade=None) :
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._grade = grade

        if self._id :
            Students.students.append(self)

        def __str__(self) :
            return f"ID: {self._id} Name: {self._first_name} {self._last_name} Age: {self._age} Grade: {self._grade}"
        
        def __repr__(self):
            return self.__str__(self)


all_students = Students()

all_students.load_students(Students.lst_students_raw)

print(Students.students)