"""
Created on Tuesday, Feb 04 2020
Author: Ejona Kocibelli
Project Description: Improved classifyTriangle function
"""


def classifyTriangle(a, b, c):
    """Function triangle_classification has three sides of a triangle as parameters and classifies the triangle if it is
         equilateral, scalene or isosceles and whether it is right triangle as well"""
    try:
        """Parameters should be numbers, raises an exception if not so"""
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return 'InvalidInput'
    else:
        [a, b, c] = sorted([a, b, c])
        if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
            return 'InvalidInput'
        else:

            if (a + b > c) and (b + c > a) and (a + c > b):  # sum of two sides should be bigger than the third side
                if round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2):
                    if a == b or b == c or c == a:  # check if triangle is right and isosceles
                        return 'Right and Isosceles Triangle'
                    elif a != b and b != c and a != c:  # check if triangle is right and scalene
                        return 'Right and Scalene Triangle'
                elif a == b == c:
                    return "Equilateral"  # check if triangle is equilateral
                elif a == b or b == c or c == a:
                    return "Isosceles"  # check if triangle is isosceles
                else:
                    return "Scalene"  # otherwise, triange is a scalene
            else:
                return 'NotATriangle'  # it is not a triangle if sides are <= 0
