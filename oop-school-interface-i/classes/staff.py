#!/usr/bin/env python3.12
"""Classes for staff module"""
from classes.person import Person
import csv

class Staff(Person):
    """Staff class"""

    # Class Methods
    @classmethod
    def all_staff(cls) :
        """Loads all staff from csv file
        
        Args:
            None
        Returns:
            (list) List of staff objects from each row in csv file
        """
        str_file = "./data/staff.csv"
        lst_result = []

        with open(str_file, mode='r') as file_csv :
            this_reader = csv.DictReader(file_csv, delimiter=",")
            for dct_row in this_reader :
                this_staff = Staff(**dct_row)
                lst_result.append(this_staff)

        return lst_result
    
    # Constructor
    def __init__(self, name=None, age=None, role=None, employee_id=None, password=None) :
        """Creates instance of Staff class
        
        Args:
            name - (str) Staff name,
            age - (int) Staff age,
            role - (str) Staff role,
            employee_id - (str) Employee ID,
            password - (str) Staff password
        Returns:
            NOne
        """
        self.employee_id = employee_id
        dct_this_person = {
            'name':name,
            'age':age,
            'role':role,
            'password':password,
        }
        super().__init__(**dct_this_person)