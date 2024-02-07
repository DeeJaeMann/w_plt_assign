#!/usr/bin/env python3.12
import re

class Student:
    """Student class for use in school registry"""
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def get_name(self) :
        """Gets the name property

        Args:
            none
        Returns:
            Student name
        """
        return self._name
    
    @get_name.setter
    def set_name(self, name) : 
        """Updates students name onl if the name is 3 or more characters, holds no spaces or special characters and is in title format
        
        Args:
            name Name to set
        Returns:
            Message only on fail
        """
        re_pattern = "^[A-Z][a-zA-Z]{2,}$"
        matches = re.match(re_pattern, f"{name}")
        if matches == None:
             print("Enter a valid name: 3 characters or more")
        else:
            self._name = name

    @property
    def get_age(self) :
        """Gets the student age

        Args:
            none
        Returns:
            Student age
        """
        return self._age

    @get_age.setter
    def set_age(self, age) :
        """Sets student age if greater than 11 or less than 18

        Args:
            age Age as an integer
        Returns:
            Message only on fail
        """
        if type(age) == int and 11 < age < 18 :
            self._age = age
        else: print("invalid")
        

    @property
    def get_grade(self) :
        """Gets student grade

        Args:
            None
        Returns:
            Student grade as string
        """
        return self._grade

    @get_grade.setter
    def set_grade(self, grade) :
        """Sets student grade if within 9-12th as a string

        Args:
            grade Student grade as string - including 'th'
        Returns:
            Message on fail
        """
        re_pattern = r'^1?\dth$'
        matches = re.match(re_pattern, f'{grade}')
        if matches == None:
             print("Enter a valid grade as string")
        elif  8 < int(grade[:-2]) < 13:
            self._grade = grade
        else: print('Outside of grade range (9-12 only)')



student = Student("Jaxson", 10, '7th')


# print(student.get_name)
# student.set_name = 'DJ'
# print(student.get_name)
# student.set_age = 13
# student.set_age = "pineapple"
#print(student.get_age)
# print(student.get_grade)
# # student.set_grade = 'not a gradeth'
# student.set_grade = '11th'
# print(student.get_grade)
