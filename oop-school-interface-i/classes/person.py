#!/usr/bin/env python3.12
"""Classes for person module"""

class Person:
    """Person class"""
    def __init__(self, name=None, age=None, role=None, password=None) :
        """Creates instance of Person class
        
        Args:
            name - (str) Person name,
            age - (int) Person age,
            role - (str) Person role,
            password - (str) Person password
        Returns:
            None
        """
        self.name = name
        self.age = int(age)
        self.role = role
        self.password = password