#!/usr/bin/python3
"""
This is module 0-lookup
This module contains one function `lookup()`
"""


def lookup(obj):
    """
    Write a function that returns the list of available
    attributes and methods of an object
    Args:
        any object
    Returns:
        a list
    """
    return dir(obj)
