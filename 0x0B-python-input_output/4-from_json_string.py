#!/usr/bin/python3
"""
the mod returns JSON String -> Object
"""


def from_json_string(my_str):
    """the func returns an object (Python data structure) -> string"""
    import json
    j_son = json.loads(my_str)
    return (j_son)
