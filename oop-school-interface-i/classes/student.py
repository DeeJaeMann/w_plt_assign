#!/usr/bin/env python3.12
"""Classes for student module"""
from classes.person import Person

class Student(Person):
    """Student class"""
    def __init__(self, name=None, age=None, school_id=None, password=None) :
        """Creates instance of Student class
        
        Args:
            name - (str) Student name,
            age - (int) Student age,
            school_id - (str) School ID,
            password - (str) Student password
        Returns:
            None
        """
        self.school_id = school_id
        super().__init__(name, age, "Student", password)