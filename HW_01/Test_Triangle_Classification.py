"""
Created on Tuesday, Jan 28 2020
Author: Ejona Kocibelli
Project Description: Triangle Classification Testing
"""
import math
import unittest
from Triangle_Classification import triangle_classification


class TestTriangles(unittest.TestCase):
    def test_wrong_inputs(self):
        """verify if function raises the exception properly when the input is incorrect"""
        with self.assertRaises(ValueError):
            triangle_classification('hello', 1, 1)
            triangle_classification('A', 'B', 'C')

    def test_not_a_triangle(self):
        """verify if the function identifies properly if the input is a triangle or no"""
        self.assertEqual(triangle_classification(1, 1, 2), 'This is not a triangle')
        self.assertEqual(triangle_classification(7, 3, 2), 'This is not a triangle')
        self.assertNotEqual(triangle_classification(3, 4, 5), 'This is not a triangle')
        self.assertEqual(triangle_classification(-1, -3, -2), 'A triangle cannot have any negative or 0 side')
        self.assertEqual(triangle_classification(0, 0, 0), 'A triangle cannot have any negative or 0 side')
        self.assertIn('This is not a triangle', triangle_classification(1, 2, 3))

    def test_right_and_scalene(self):
        """verify if the function determines properly if the triangle is right and scalene"""
        self.assertEqual(triangle_classification(3, 4, 5), 'Right and Scalene Triangle')
        self.assertEqual(triangle_classification(3, 5, 4), 'Right and Scalene Triangle')
        self.assertNotEqual(triangle_classification(4, 3, 6), 'Right and Scalene Triangle')
        self.assertEqual(triangle_classification(3000000, 4000000, 5000000), 'Right and Scalene Triangle')

    def test_right_and_isosceles(self):
        """verify if the function determines properly if the triangle is right and isosceles"""
        self.assertEqual(triangle_classification(1, 1, math.sqrt(2)), 'Right and Isosceles Triangle')
        self.assertNotEqual(triangle_classification(3, 5, 5), 'Right and Isosceles Triangle')
        self.assertTrue(triangle_classification(2147483647, 2147483647, 5) == 'Right and Isosceles Triangle')
        self.assertEqual(triangle_classification(3, 3, 4.242640687119285146), 'Right and Isosceles Triangle')

    def test_equilateral(self):
        """verify if the function determines properly if the triangle is equilateral"""
        self.assertEqual(triangle_classification(1, 1, 1), 'Equilateral Triangle')
        self.assertEqual(triangle_classification(3.33, 3.33, 3.33), 'Equilateral Triangle')
        self.assertNotEqual(triangle_classification(3.33, 3.33, 3.333), 'Equilateral Triangle')
        self.assertEqual(triangle_classification(1e0, 1e0, 1e0), 'Equilateral Triangle')

    def test_isosceles(self):
        """verify if the function determines properly if the triangle is isosceles,"""
        self.assertEqual(triangle_classification(4, 4, 5), 'Isosceles Triangle')
        self.assertEqual(triangle_classification(1234567890, 1234567890, 987654321), 'Isosceles Triangle')
        self.assertNotEqual(triangle_classification(3, 4, 5), 'Isosceles Triangle')
        self.assertNotEqual(triangle_classification(2, 2, 2.0000000000000001), 'Isosceles Triangle')  # precision failure
        self.assertEqual(triangle_classification(2, 2, 2.000000000000001), 'Isosceles Triangle')
        self.assertEqual(triangle_classification(2, 2, 2.0000000000000001), 'Equilateral Triangle')

    def test_scalene(self):
        """verify if the function determines properly if the triangle is scalene"""
        self.assertEqual(triangle_classification(3, 4, 6), 'Scalene Triangle')
        self.assertEqual(triangle_classification(3*2 ^ 64, 4*2 ^ 64, 5*2 ^ 64), 'Scalene Triangle')  # PEMDAS failure
        self.assertNotEqual(triangle_classification(3 * (2 ^ 64), 4 * (2 ^ 64), 5 * (2 ^ 64)), 'Scalene Triangle')
        self.assertEqual(triangle_classification(3 * (2 ^ 64), 4 * (2 ^ 64), 5 * (2 ^ 64)), 'Right and Scalene Triangle')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
