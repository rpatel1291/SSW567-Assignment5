import unittest
import pytest

from Triangle import classify_triangle, valid_input


class TestTriangle(unittest.TestCase):

    def testValidInputs(self):
        self.assertEqual(valid_input(-1, 2, 3), False, "-1,2,3 are invalid inputs for a triangle")

    def testValidInputs2(self):
        self.assertEqual(valid_input(1, 2, 3), True, "1,2,3 are invalid inputs for a triangle")

    def testValidInputs3(self):
        self.assertEqual(valid_input(3, 4, 5), True, "3,4,5 are valid inputs for a triangle")

    def testTriangle1(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'Isoceles', '1,2,3 is not a triangle')

    def testTriangle2(self):
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral', '3,3,3 is a equilateral triangle')

    def testTriangle3(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a right triangle')



if __name__ == '__main__':
    unittest.main()
