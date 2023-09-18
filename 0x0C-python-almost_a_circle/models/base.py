#!/usr/bin/python3
"""Base class module"""
import json
import turtle
import random


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json serialization of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                jf.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with attributes set from dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Return list of instances from file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jf:
                dicts = cls.from_json_string(jf.read())
                return [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as cf:
            if list_objs is None:
                cf.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                cf.write(Base.to_json_string(dicts))

    @classmethod
    def load_from_file_csv(cls):
        """Load from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as cf:
                dicts = cls.from_json_string(cf.read())
                return [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using turtle"""
        colors = ["red", "blue", "yellow", "orange", "purple", "green"]
        turt = turtle.Turtle()
        turt.screen.bgcolor("white")
        turt.pensize(5)
        turt.speed(5)
        turt.hideturtle()
        for rec in list_rectangles:
            turt.color(random.choice(colors))
            turt.penup()
            turt.goto(rec.x, rec.y)
            turt.pendown()
            for i in range(2):
                turt.forward(rec.width)
                turt.right(90)
                turt.forward(rec.height)
                turt.right(90)
        for sqr in list_squares:
            turt.color(random.choice(colors))
            turt.penup()
            turt.goto(sqr.x, sqr.y)
            turt.pendown()
            for i in range(4):
                turt.forward(sqr.width)
                turt.right(90)
        turtle.exitonclick()
