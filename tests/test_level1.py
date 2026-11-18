import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    # Arrange, Act, Assert

    def test_sum(self):
        # Arrange
        testCal = Calculator(8,2)

        # Act and assert
        self.assertEqual(testCal.get_sum(), 10, "The sum is wrong")

    def test_difference(self):
        # Arrange
        testCal = Calculator(8,2)

        # Act and assert
        self.assertEqual(testCal.get_difference(), 6, "The difference is wrong")

    def test_product(self):
        # Arrange
        testCal = Calculator(8,2)

        # Act and assert
        self.assertEqual(testCal.get_product(), 16, "The product is wrong")

    def test_quotient(self):
        # Arrange
        testCal = Calculator(8,2)

        # Act and assert
        self.assertEqual(testCal.get_quotient(), 4, "The quotient is wrong")

if __name__ == "__main__":
    unittest.main()