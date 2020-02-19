"""
Created on Tuesday, Jan 28 2020
Author: Ejona Kocibelli
Project Description: Triangle Classification Implementation
"""


def triangle_classification(a, b, c):
    """Function triangle_classification has three sides of a triangle as parameters and classifies the triangle if it is
     equilateral, scalene or isosceles and whether it is right triangle as well"""
    try:
        """Parameters should be numbers, raises an exception if not so"""
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise ValueError("Each side of triangle has to be a number!")
    else:
        [a, b, c] = sorted([a, b, c])  # add the parameters in a list, and sort the list
        if a > 0 and b > 0 and c > 0:  # parameters should be greater than 0 to be side of triangles
            if (a + b > c) and (b + c > a) and (a + c > b):  # sum of two sides should be bigger than the third side
                if round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2):
                    if a == b or b == c or c == a:  # check if triangle is right and isosceles
                        return 'Right and Isosceles Triangle'
                    elif a != b and b != c and a != c:  # check if triangle is right and scalene
                        return 'Right and Scalene Triangle'
                    else:
                        return 'Right'
                elif a == b == c:
                    return "Equilateral Triangle"  # check if triangle is equilateral
                elif a == b or b == c or c == a:
                    return "Isosceles Triangle"  # check if triangle is isosceles
                else:
                    return "Scalene Triangle"  # otherwise, triange is a scalene
            else:
                return "This is not a triangle"  # it is not a triangle if does not complete the triangle sides rule
        else:
            return 'A triangle cannot have any negative or 0 side'  # it is not a triangle if sides are <= 0

