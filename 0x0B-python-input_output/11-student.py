#!/usr/bin/python3
"""
the module creates a class Student
"""


class Student:
    """the class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of attr for first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__.keys():
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json.keys():
            self.__dict__[key] = json[key]
