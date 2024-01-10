#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """check if an object is exactly an instance of a class.

    Args:
        obj:The object to check.
        a_class(type): the class to match the type of an obj.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
