import unittest 
from app import fibonacchi, factorial


class TestFibonnachi(unittest.TestCase):
    def test_fibonacchi_1(self):
        self.assertEqual(fibonacchi(1), 1)

class TestFibonnachi_10(unittest.TestCase):
    def test_fibonacchi_10(self):
        self.assertEqual(fibonacchi(10), 89)

class TestFibonnachi_30(unittest.TestCase):
    def test_fibonacchi_30(self):
        self.assertEqual(fibonacchi(30), 1346269)

class factorial_1(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)


# if __name__ == '__main__':
#     unittest.main()