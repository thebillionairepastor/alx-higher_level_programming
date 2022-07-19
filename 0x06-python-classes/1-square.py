#!/usr/bin/python3
"""Module that define the class Square with the private attrivute size"""


class Square:
    """class Square with a private attrivute size"""
    __size = ""

    """function that define the private attrivute size"""
    def __init__(self, size):
        self.__size = size
