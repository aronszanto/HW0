# Filename: util.py
# Author: Aron Szanto
# Date: 9/1/16
# Email: aszanto@college.harvard.edu

import copy
from collections import deque

# Problem 1


def matrix_multiply(x, y):
    # general solution to matrices of any compatible size
    # fun with nested comprehensions and argument unpacking!
    return [[sum(a * b for (a,b) in zip(row,col)) for col in zip(*y)] for row in x]

# Problem 2, 3


class MyQueue:

    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __str__(self):
        pass


class MyStack:

    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __str__(self):
        pass

# Problem 4


def add_position_iter(lst, number_from=0):
    pass


def add_position_recur(lst, number_from=0):
    pass


def add_position_map(lst, number_from=0):
    pass

# Problem 5


def remove_course(roster, student, course):
    pass

# Problem 6


def copy_remove_course(roster, student, course):
    pass
