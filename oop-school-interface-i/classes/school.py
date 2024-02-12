#!/usr/bin/env python3.12
"""Classes for school module"""
from classes.student import Student
from classes.staff import Staff
from classes.person import Person

class School:
    """School class"""
    def __init__(self, name):
        """Creates instance of School class
        
        Args:
            name - (str) School Name
        Returns:
            None
        """
        self.name = name
        self.staff = []
        self.students = Student.all_students()



