#!/usr/bin/python3
''' Defines a class Student.'''


class Student:
    ''' a Student class.'''

    def __init__(self, first_name, last_name, age):
        '''Initailization.

        Args:
            first_name(str): The first name of the student.
            last_name(str): The second name of the student.
            age(int): The age of the student.
        Retuens:
            None
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student.

        Args:
            attrs (list): (Optional) The attributes to represent.

        '''
        if (type(attrs) == list and
                all(type(elt) == str for elt in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
