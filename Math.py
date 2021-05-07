import unittest
import math
from Math import my_fabs



class TestMath(unittest.TestCase):
    """

    """

    def test_correct_param(self):
        input_result = -4.23
        expected = 4.23
        self.assertEqual(math.fabs(input_result), expected)


    def test_positive_param(self):
        input_result = 7.2
        expected = 7.2
        self.assertEqual(math.fabs(input_result), expected)



    def test_missing_param(self):
        "Test for missing parameters"
        with self.assertRaises(TypeError):
            self.assertEqual(my_fabs(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(my_fabs(''), True)


    def test_wrong_param(self):
        "Test for wrong parameters"
        with self.assertRaises(TypeError):
            my_fabs({})
        with self.assertRaises(TypeError):
            my_fabs([])
        with self.assertRaises(TypeError):
            my_fabs("Wrong String")


"If you run this module (-m) directly, then run the code within the conditional, the unittest.main runs everything"
if __name__ == '__main__': 
    unittest.main()
