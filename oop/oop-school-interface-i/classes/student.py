#!/usr/bin/env python3.12
"""Classes for student module"""
from classes.person import Person
import csv

class Student(Person):
    """Student class"""

    # Class Methods
    @classmethod
    def all_students(cls) :
        """Loads all students from csv file
        
        Args:
            None
        Returns:
            (list) List of student objects from each row in csv file
        """
        str_file = "./data/students.csv"
        lst_result = []

        with open(str_file, mode='r') as file_csv :
            this_reader = csv.DictReader(file_csv, delimiter=",")
            for dct_row in this_reader :
                this_student = Student(**dct_row)
                lst_result.append(this_student)

        return lst_result

    # Constructor
    def __init__(self, name=None, age=None, role='Student', school_id=None, password=None) :
        """Creates instance of Student class
        
        Args:
            name - (str) Student name,
            age - (int) Student age,
            role - (str) Student role
            school_id - (str) School ID,
            password - (str) Student password
        Returns:
            None
        """
        self.school_id = school_id
        dct_this_person = {
            'name':name,
            'age':age,
            'role':role,
            'password':password,
        }
        super().__init__(**dct_this_person)