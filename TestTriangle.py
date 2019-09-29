import unittest
import pytest

from Triangle import classifyTraingle, validInput

class TestTriangle(unittest.TestCase):
    def testValidInputs(self):
       self.assertEqual(validInput(-1,2,3), False, "-1,2,3 are invalid inputs for a triangle")
    def testValidInputs2(self):
        self.assertEqual(validInput(1,2,3), False, "1,2,3 are invalid inputs for a triangle")
    def testValidInputs3(self):
        self.assertEqual(validInput(3,4,5), True, "3,4,5 are valid inputs for a triangle")
    def testTriangle1(self):
        self.assertEqual(classifyTraingle(1,2,3),'NotATriangle', '1,2,3 is not a triangle')
    def testTrangle2(self):
        self.assertEqual(classifyTraingle(3,3,3), 'Equilateral', '3,3,3 is a equilateral triangle')
    def testTriangle3(self):
        self.assertEqual(classifyTraingle(3,4,5), 'RightIsoceles', '3,4,5 is a right and isoceles triangle')
    def testTriangle4(self):
        self.assertEqual(classifyTraingle(2,2,8**.5), 'RightScalene', '2,2,sqrt(8) is a right and scalene triangle')

if __name__ == '__main__':
    unittest.main()
