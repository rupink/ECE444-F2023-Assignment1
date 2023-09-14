print("Hello World 6")

import unittest
from utils import utils

class TestUtils(unittest.TestCase):

    def test_reversed_with_integers(self):
        self.assertEqual(Utils.reversed(12345), 54321)
        self.assertEqual(Utils.reversed(987654321), 123456789)
    
    def test_reversed_with_non_integer(self):
        with self.assertRaises(ValueError):
            Utils.reversed("12345")
        with self.assertRaises(ValueError):
            Utils.reversed(12.345)

    def test_formatter_with_integers(self):
        self.assertEqual(Utils.formatter(10), {"binary": '0b1010', "octal": '0o12'})
        self.assertEqual(Utils.formatter(255), {"binary": '0b11111111', "octal": '0o377'})

    def test_formatter_with_non_integer(self):
        with self.assertRaises(ValueError):
            Utils.formatter("12345")
        with self.assertRaises(ValueError):
            Utils.formatter(12.345)

if __name__ == "__main__":
    unittest.main()