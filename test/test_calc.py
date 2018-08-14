import sys, os, unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import calc

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.addition(10, 20), 30) # For Positive with Positive
        self.assertEqual(calc.addition(1, -1), 0) # For Positive with Negative
        self.assertEqual(calc.addition(-1, -1), -2) # For Negative with Negative

    def test_subtraction(self):
        self.assertEqual(calc.subtraction(10, 20), -10)
        self.assertEqual(calc.subtraction(1, -1), 2)
        self.assertEqual(calc.subtraction(-1, -1), 0)

    def test_summation(self):
        self.assertEqual(calc.summation(10, 20), 200)
        self.assertEqual(calc.summation(1, -1), -1)
        self.assertEqual(calc.summation(-1, -1), 1)

    def test_division(self):
        self.assertEqual(calc.division(10, 20), 0.5)
        self.assertEqual(calc.division(1, -1), -1)
        self.assertEqual(calc.division(-1, -1), 1)
        self.assertEqual(calc.division(3, 2), 1.5) # For floor division

        # Testing of division by Zero
        with self.assertRaises(ValueError):
            calc.division(10, 0)
    
if __name__ == "__main__":
    unittest.main()
    
