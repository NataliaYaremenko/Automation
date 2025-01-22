import unittest
from homeworks import (operation, together, computer_price, all)

class TestOperation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_apples = 2
        cls.invalid_apples = [-1, 'apple']

    def setUp(self):
        self.expected_valid = 8
        self.expected_invalid = "Do it again, bananas should be in 4 times more than apples"

    def test_valid_input(self):
        from homeworks import operation
        result = operation(self.valid_apples)
        self.assertEqual(result, self.expected_valid)

    def test_invalid_input(self):
        from homeworks import operation
        result = operation(self. invalid_apples)
        self.assertEqual(result, self.expected_invalid)

class TestTogether(unittest.TestCase):

    def test_add_positive_number_AzovBlack(self):
        self.assertEqual(together(436402, 37800), 474202)

    def test_add_negative_number_AzovBlack(self):
        self.assertEqual(together(-436402, -37800), 474202)

    def test_add_mixed_number_AzovBlack(self):
        self.assertEqual(together(-436402, 37800), -3800)
        self.assertEqual(together(-37800, 436402), 58469)

class TestComputer_price(unittest.TestCase):

    def test_computer_price_True(self):
        self.assertTrue(computer_price(18, 1179), 21222)

    def test_computer_price_False(self):
        self.assertFalse(computer_price(18, 1179), 56985)

class TestAll(unittest.TestCase):

    def test_all_price_right(self):
        self.assertEqual(all(232, 8), 29.0)

    def test_all_price_Notright(self):
        self.assertEqual(all(232, 8), 1)

if __name__ == '__main__':
    unittest.main()