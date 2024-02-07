#!/usr/bin/env python3.12
import re

class Student:
    """Student class for use in school registry"""
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self) :
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"

    # Helper methods
    def convert_grade(self, grade) :
        return int(grade[:-2])

    # Getters and Setters
    @property
    def get_name(self) :
        """Gets the name property

        Args:
            none
        Returns:
            Student name
        """
        return self._name.capitalize()
    
    @get_name.setter
    def set_name(self, name) : 
        """Updates students name only if the name is 3 or more characters, holds no spaces or special characters and is in title format
        
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
        elif  8 < self.convert_grade(grade) < 13:
            self._grade = grade
        else: print("Outside of grade range (9-12 only)")

    # Methods
        

    
    def advance(self, years = 1) :
        """Adds years to current grade if valid

        Args:
            years Number of years to add
        Returns:
            Success or Fail message
        """
        grade = self.convert_grade(self.get_grade)

        grade += years

        grade = f"{grade}th"
        # Calls grade into grade setting and captures any invalid entry output into grade_result
        grade_result = self.set_grade = grade

        if not grade_result :
            return f"{self.get_name} has advanced to the {self.get_grade} grade"

    def study(self, subject) :
        pass


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
print(student)
student.advance(3)
print(student)
