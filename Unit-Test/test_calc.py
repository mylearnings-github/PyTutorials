# To run the test w/o any setting:
# (base) K:\DSA\CoreySchafer-PythonCourse\Unit-Test>python -m unittest test_calc.py



import unittest
import calc

# print(dir(calc))
 
class TestCalc(unittest.TestCase):
    """
        Assert Methods Reference - https://docs.python.org/3.9/library/unittest.html
    """
    def test_add(self):
        """
            Name of the method is important, it has to be test_<methodname>
        """
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):

        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):

        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):

        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # or, use context manager as shown below:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
