#!/usr/bin/python3
import json
"""
This is module 3-to_json_string

This module contains one function `to_json_string`
"""


def to_json_string(my_obj):
    """
    function that returns JSON representation
    of an object (string):
    You don't need to manage exceptions if
    the object can't be serialized.

    Args:
    my_obj

    Return:
    JSON representation of object
    """
    return json.dumps(my_obj)
