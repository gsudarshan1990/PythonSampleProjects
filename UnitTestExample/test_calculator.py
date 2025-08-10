import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        result = calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        result = calculator.add(-5, -3)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers"""
        result = calculator.add(10, -3)
        self.assertEqual(result, 7)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers"""
        result = calculator.subtract(10, 3)
        self.assertEqual(result, 7)

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number"""
        result = calculator.subtract(3, 10)
        self.assertEqual(result, -7)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers"""
        result = calculator.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_multiply_by_zero(self):
        """Test multiplication by zero"""
        result = calculator.multiply(5, 0)
        self.assertEqual(result, 0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers"""
        result = calculator.multiply(-3, 4)
        self.assertEqual(result, -12)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers"""
        result = calculator.divide(15, 3)
        self.assertEqual(result, 5.0)

    def test_divide_with_float_result(self):
        """Test division resulting in float"""
        result = calculator.divide(10, 3)
        self.assertAlmostEqual(result, 3.333333333333333, places=10)

    def test_divide_by_zero_raises_exception(self):
        """Test that division by zero raises ValueError"""
        with self.assertRaises(ValueError) as context:
            calculator.divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_power_positive_numbers(self):
        """Test power calculation with positive numbers"""
        result = calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_with_zero_exponent(self):
        """Test power calculation with zero exponent"""
        result = calculator.power(5, 0)
        self.assertEqual(result, 1)

    def test_power_with_negative_exponent(self):
        """Test power calculation with negative exponent"""
        result = calculator.power(2, -2)
        self.assertEqual(result, 0.25)

    def test_factorial_positive_numbers(self):
        """Test factorial of positive numbers"""
        self.assertEqual(calculator.factorial(0), 1)
        self.assertEqual(calculator.factorial(1), 1)
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_negative_number_raises_exception(self):
        """Test that factorial of negative number raises ValueError"""
        with self.assertRaises(ValueError) as context:
            calculator.factorial(-1)
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers")

    def test_is_prime_small_numbers(self):
        """Test prime checking for small numbers"""
        self.assertFalse(calculator.is_prime(0))
        self.assertFalse(calculator.is_prime(1))
        self.assertTrue(calculator.is_prime(2))
        self.assertTrue(calculator.is_prime(3))
        self.assertFalse(calculator.is_prime(4))
        self.assertTrue(calculator.is_prime(5))

    def test_is_prime_larger_numbers(self):
        """Test prime checking for larger numbers"""
        self.assertTrue(calculator.is_prime(17))
        self.assertTrue(calculator.is_prime(23))
        self.assertFalse(calculator.is_prime(25))
        self.assertFalse(calculator.is_prime(100))

    def test_average_positive_numbers(self):
        """Test average calculation with positive numbers"""
        numbers = [1, 2, 3, 4, 5]
        result = calculator.average(numbers)
        self.assertEqual(result, 3.0)

    def test_average_mixed_numbers(self):
        """Test average calculation with mixed positive/negative numbers"""
        numbers = [-2, -1, 0, 1, 2]
        result = calculator.average(numbers)
        self.assertEqual(result, 0.0)

    def test_average_single_number(self):
        """Test average calculation with single number"""
        numbers = [42]
        result = calculator.average(numbers)
        self.assertEqual(result, 42.0)

    def test_average_empty_list_raises_exception(self):
        """Test that average of empty list raises ValueError"""
        with self.assertRaises(ValueError) as context:
            calculator.average([])
        self.assertEqual(str(context.exception), "Cannot calculate average of empty list")

    def test_floating_point_operations(self):
        """Test operations with floating point numbers"""
        result = calculator.add(1.5, 2.3)
        self.assertAlmostEqual(result, 3.8, places=1)
        
        result = calculator.multiply(2.5, 4.0)
        self.assertEqual(result, 10.0)

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.test_numbers = [1, 2, 3, 4, 5]
        self.negative_numbers = [-5, -3, -1]

    def tearDown(self):
        """Clean up after each test method"""
        pass  # No cleanup needed for this example


if __name__ == '__main__':
    # Run tests with more verbose output
    unittest.main(verbosity=2)
