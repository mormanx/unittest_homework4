import unittest
from utils.arrs import get, my_slice
class TestArrs(unittest.TestCase):
    def test_get_positive_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(get(arr, 1, "test"), 2)
    def test_get_negative_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(get(arr, -1, "test"), "test")
    def test_get_empty_index(self):
        arr = []
        self.assertEqual(get(arr, 0, "test"), "test")
    def test_get_zero_index(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, 0, "test"), 1)
    def test_get_out_of_range_index(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, 10, "test"), "test")
    def test_get_negative_out_of_range_index(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, -10, "test"), "test")
    def test_my_slice_positive_all_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1, 3), [2, 3])
    def test_my_slice_positive_start_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1), [2, 3, 4])
    def test_my_slice_negative_start_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, -1), [4])
    def test_my_slice_negative_end_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1, -3), [])
    def test_my_slice_negative_all_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, -3, -1), [2, 3])
    def test_my_slice_negative_all_index_out_of_range(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, -5, -1), [1, 2, 3])
    def test_my_slice_negative_end_index_out_of_range(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1, -6), [])
    def test_my_slice_zero_index(self):
        arr = [1, 2, 3]
        self.assertEqual(my_slice(arr, 1), [2, 3])
    def test_my_slice_empty_index(self):
        arr = []
        self.assertEqual(my_slice(arr, 1), [])
    def test_my_slice_empty_empty_index(self):
        arr = [1, 2]
        self.assertEqual(my_slice(arr), [1, 2])
    def test_my_slice_full_slice(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr), [1, 2, 3, 4])
    def test_my_slice_out_of_range_start_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 10), [])
    def test_my_slice_out_of_range_end_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1, 10), [2, 3, 4])
    def test_my_slice_negative_out_of_range_start_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, -10), [1, 2, 3, 4])
    def test_my_slice_negative_out_of_range_end_index(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(my_slice(arr, 1, -10), [])
if __name__ == '__main__':
    unittest.main()