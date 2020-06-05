#!/usr/bin/python3
"""
 function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    args: obj = object to look, a_class = expected super class object
    """
    for parent in obj.__class__.__bases__:
        if issubclass(parent, a_class):
            return True
    return False
