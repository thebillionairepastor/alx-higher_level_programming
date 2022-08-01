#!/usr/bin/python3
"""
This is module 9-rectangle

This module contains:
-one class
-two functions
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits class from BaseGeometry (7-base_geometry)

    Instantiation with width and height:
    def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator

    Args:
    width
    height
    Returns:
    area of shape
    """

    def __init__(self, width, height):
        """
        private instantiation
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """
        returns the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        instance method for string - print class name with
        following rectangle description: [Rectangle] <width>/<height>
        """
        return ("[{:s}] {:d}/{:d}".
                format(self.__class__.__name__,
                       self.__width,
                       self.__height))
