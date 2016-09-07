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
    return [[sum(a * b for (a, b) in zip(row, col)) for col in zip(*y)] for row in x]

# Problem 2, 3


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        return self.queue.popleft() if len(self.queue) != 0 else None

    def __eq__(self, other):
        return list(self.queue) == list(other.queue)

    def __ne__(self, other):
        return list(self.queue) != list(other.queue)

    def __str__(self):
        return str(list(self.queue))


class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop() if len(self.stack) != 0 else None

    def __eq__(self, other):
        return list(self.stack) == list(other.stack)

    def __ne__(self, other):
        return list(self.stack) != list(other.stack)

    def __str__(self):
        return str(list(self.stack))

# Problem 4


def add_position_iter(lst, number_from=0):
    return [n + i + number_from for i, n in enumerate(lst)]


def add_position_recur(lst, number_from=0):
    def f(l, n, i):
        return [l[0] + n + i] + f(l[1:], n, i + 1) if len(l) > 1 else [l[0] + n + i]
    return f(lst, number_from, 0)


def add_position_map(lst, number_from=0):
    return map(lambda (i, x): x + i + number_from, enumerate(lst))
# Problem 5


def remove_course(roster, student, course):
    roster[student].remove(course)
    return roster

# Problem 6


def copy_remove_course(roster, student, course):
    return remove_course(copy.deepcopy(roster), student, course)
