import unittest
from index import most_frequent_elements

class TestMostFrequentElements(unittest.TestCase):
    def test_basic_case(self):
        nums = [10, 20, 30, 20, 10, 10, 30, 30, 30]
        expected_output = [20, 10, 30]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_all_elements_unique(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_all_elements_same(self):
        nums = [7, 7, 7, 7, 7]
        expected_output = [7]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_empty_list(self):
        nums = []
        expected_output = []  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_tie_in_frequency(self):
        nums = [1, 1, 2, 2, 3, 3, 4]
        expected_output = [4, 1, 2, 3]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_large_input(self):
        nums = [5, 5, 5, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1]
        expected_output = [5, 2, 3, 1]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_negative_numbers(self):
        nums = [-1, -2, -2, -3, -3, -3]
        expected_output = [-1, -2, -3]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

    def test_mixed_numbers(self):
        nums = [0, 0, -1, -1, -1, 2, 2, 2, 2]
        expected_output = [0, -1, 2]  
        self.assertEqual(most_frequent_elements(nums), expected_output)

if __name__ == "__main__":
    unittest.main()
