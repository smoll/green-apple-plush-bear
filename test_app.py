import unittest
from app import diff_max_and_min

class AppTestCases(unittest.TestCase):
    """Tests for `app.py`."""

    def test_example_one(self):
        """Diff example one"""
        self.assertEqual(diff_max_and_min([1, 2, 3, 4, 5]), 4)

    def test_example_two(self):
        """Diff example two"""
        self.assertEqual(diff_max_and_min([100, 150, 215, 80, 152]), None)

    def test_example_three(self):
        """Diff example three"""
        self.assertEqual(diff_max_and_min([3000, 4, 0, 9, 500]), 3000)

if __name__ == '__main__':
    unittest.main()
