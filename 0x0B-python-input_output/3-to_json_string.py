#!/usr/bin/python3
"""
the mod returns the JSON of an object (str)
"""


def to_json_string(my_obj):
    """The func returns the JSON of an object"""
    import json
    j_son = json.dumps(my_obj)
    return (j_son)
