#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """Prevent the user from making new inst attr"""
    __slots__ = ["first_name"]
