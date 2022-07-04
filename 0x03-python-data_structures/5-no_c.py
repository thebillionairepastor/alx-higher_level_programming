#!/usr/bin/python3
def no_c(my_string):
    to_quit = ['c', 'C']
    newString = ''.join(i for i in my_string if i not in to_quit)
    return newString
