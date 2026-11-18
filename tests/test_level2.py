import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    # Arrange, Act, Assert

    def setUp(self):
        # Arrange
        self.calc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 10, "The sum is wrong")

    def tearDown(self):
        # Optional - allows you to destroy anything created by tests, e.g. tables
        pass

if __name__ == "__main__":
    unittest.main()