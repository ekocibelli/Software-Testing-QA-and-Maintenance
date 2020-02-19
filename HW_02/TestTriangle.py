import unittest
import math
from Improved_Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    def test_wrong_inputs(self):
        """verify if function raises the exception properly when the input is incorrect"""
        self.assertEqual(classifyTriangle('hello', 1, 1), 'InvalidInput')
        self.assertEqual(classifyTriangle('A', 'B', 'C'), 'InvalidInput')

    def test_not_a_triangle(self):
        """verify if the function identifies properly if the input is a triangle or no"""
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle')
        self.assertEqual(classifyTriangle(7, 3, 2), 'NotATriangle')
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'NotATriangle')
        self.assertEqual(classifyTriangle(-1, -3, -2), 'InvalidInput')
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput')
        self.assertIn('NotATriangle', classifyTriangle(1, 2, 3))

    def test_right_and_scalene(self):
        """verify if the function determines properly if the triangle is right and scalene"""
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right and Scalene Triangle')
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right and Scalene Triangle')
        self.assertNotEqual(classifyTriangle(4, 3, 6), 'Right and Scalene Triangle')
        self.assertEqual(classifyTriangle(3000000, 4000000, 5000000), 'InvalidInput')

    def test_right_and_isosceles(self):
        """verify if the function determines properly if the triangle is right and isosceles"""
        self.assertEqual(classifyTriangle(1, 1, math.sqrt(2)), 'Right and Isosceles Triangle')
        self.assertNotEqual(classifyTriangle(3, 5, 5), 'Right and Isosceles Triangle')
        self.assertTrue(classifyTriangle(2147483647, 2147483647, 5) == 'InvalidInput')
        self.assertEqual(classifyTriangle(3, 3, 4.242640687119285146), 'Right and Isosceles Triangle')

    def test_equilateral(self):
        """verify if the function determines properly if the triangle is equilateral"""
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classifyTriangle(3.33, 3.33, 3.33), 'Equilateral')
        self.assertNotEqual(classifyTriangle(3.33, 3.33, 3.333), 'Equilateral')
        self.assertEqual(classifyTriangle(1e0, 1e0, 1e0), 'Equilateral')

    def test_isosceles(self):
        """verify if the function determines properly if the triangle is isosceles,"""
        self.assertEqual(classifyTriangle(4, 4, 5), 'Isosceles')
        self.assertEqual(classifyTriangle(1234567890, 1234567890, 987654321), 'InvalidInput')
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'Isosceles')
        self.assertNotEqual(classifyTriangle(2, 2, 2.0000000000000001),
                            'Isosceles Triangle')
        self.assertEqual(classifyTriangle(2, 2, 2.000000000000001), 'Isosceles')
        self.assertEqual(classifyTriangle(2, 2, 2.0000000000000001), 'Equilateral')

    def test_scalene(self):
        """verify if the function determines properly if the triangle is scalene"""
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene')
        self.assertEqual(classifyTriangle(3, 6, 4), 'Scalene')
        self.assertNotEqual(classifyTriangle(3 * (2 ^ 64), 4 * (2 ^ 64), 5 * (2 ^ 64)),
                            'Scalene')
        self.assertEqual(classifyTriangle(3 * (2 ^ 64), 4 * (2 ^ 64), 5 * (2 ^ 64)),
                         'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
