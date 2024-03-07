import math


def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError('Length and width must be positive numbers')
    return length * width