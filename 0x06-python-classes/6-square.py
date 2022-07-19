#!/usr/bin/python3
"""Module that declare class Square with a private instance attribute size:"""


class Square:
    """class Square with a private attrivute size"""

    def __init__(self, size=0):
        """Function to validade of the size square"""
        self.__size = size

    @property
    def size(self):
        """Function to validade of the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function to validade the value of size,
        in case that been different of integer and less to zero"""
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    def area(self):
        """Function to return of the area square"""
        return self.__size * self.__size

    def my_print(self):
        """Function that print of the square with a symbol #"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for i in range(0, self.__size - 1):
                print("#", end="")
            print("#", end="")
            print()
