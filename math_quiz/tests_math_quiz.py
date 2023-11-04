import unittest
from math_quiz import rand_int, rand_arithmetic_symbol, calculation


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_arithmetic_symbol(self):
        for _ in range(1000):
            rand_symbol = rand_arithmetic_symbol()
            self.asserTrue(rand_symbol == '+' or rand_symbol == '-' or rand_symbol == '*')
        pass

    def test_calculation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 5, '+', '5 + 5', 10),
            (5, 3, '-', '5 - 3', 2),
            (5, 2, '*', '5 * 2', 10),
            (5, 4, '+', '5 + 4', 9),
            (2, 2, '+', '5 + 2', 7),
            (12, 2, '+', '12 + 2', 14),
            (3, 2, '-', '3 - 2', 1),
            (6, 2, '*', '6 * 2', 12),
            (4, 2, '+', '4 + 2', 6),
            (4, 2, '-', '4 - 2', 2),
            (3, 2, '*', '3 * 2', 6),
            (7, 2, '-', '7 - 2', 5),
            (8, 2, '+', '8 + 2', 10),
            (4, 2, '*', '4 * 2', 8),
            (3, 2, '+', '3 + 2', 5)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            calc, solu = calculation(num1, num2, operator)
            self.assertTrue(calc == expected_problem)
            self.assertTrue(solu == expected_answer)



if __name__ == "__main__":
    unittest.main()
