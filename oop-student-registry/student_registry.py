#!/usr/bin/env python3.12
class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def get_name(self) :
        return self._name
    
    @get_name.setter
    def set_name(self, name) :
        pass

    @property
    def get_age(self) :
        return self._age

    @get_age.setter
    def set_age(self, age) :
        pass

    @property
    def get_grade(self) :
        return self._grade

    @get_grade.setter
    def set_grade(self, grade) :
        pass



student = Student("Jaxson", 10, '7th')


print(student.get_name)
print(student.get_age)
print(student.get_grade)
