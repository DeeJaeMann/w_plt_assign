#!/usr/bin/env python3.12
"""Classes for staff module"""
from classes.person import Person

class Staff(Person):
    """Staff class"""
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