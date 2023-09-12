#!/usr/bin/python3
def load_from_json_file(filename):
    """the func creates an Object from a “JSON file”"""
    import json
    with open(filename, 'r') as f:
        return (json.load(f))
