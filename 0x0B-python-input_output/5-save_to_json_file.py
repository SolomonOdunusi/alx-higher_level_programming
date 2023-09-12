#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """the func saves an object (Python data structure) -> string"""
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
