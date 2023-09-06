#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """Prevent the user from making new inst attr"""
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
