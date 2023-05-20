import unittest
from utils.arrs import get, my_slice


class TestArrs(unittest.TestCase):
    def test_get_positive_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(get(arr, 1, "test"), 2)

    def test_get_zero_index(self):
        arr = []
        self.assertEqual(get(arr, 0, "test"), "test")

    def test_myslice_test_positive_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1, 3), [2, 3])

    def test_myslice_test_zero_index(self):
        arr = [1, 2, 3]
        self.assertEqual(my_slice(arr, 1), [2, 3])


if __name__ == '__main__':
    unittest.main()
