#!/usr/bin/env python3.12
"""Classes for staff module"""
from person import Person

class Staff(Person):
    """Staff class"""
    def __init__(self, name, age, role, employee_id, password) :
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
        self.employee_id - employee_id
        super().__init__(name, age, role, password)