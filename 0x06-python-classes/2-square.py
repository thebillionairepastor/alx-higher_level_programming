#!/usr/bin/python3
"""Module that declare class Square with a private instance attribute size:"""


class Square:
    """class Square with a private attrivute size"""
    def __init__(self, size=0):
        """Function to validade of the size square"""
        self.__size = size
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
