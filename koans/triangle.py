#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if min(a, b, c) <= 0:
        raise TriangleError
    if max(a, b, c) > sum((a, b, c)) / 2:
        raise TriangleError
    answer = {1: "equilateral", 2: "isosceles", 3: "scalene"}
    sides_count = len(set([a, b, c]))
    return answer.get(sides_count, None)


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
