import unittest
from insertion_sort import InsertionSort, SortingClient

class InsertionSortTest(unittest.TestCase):
    def test_sort(self):
        algorithm = InsertionSort()
        data = [5, 2, 7, 1, 8]
        algorithm.sort(data)
        self.assertEqual(data, [1, 2, 5, 7, 8])

class SortingClientTest(unittest.TestCase):
    def test_sort_data(self):
        algorithm = InsertionSort()
        client = SortingClient(algorithm)
        data = [5, 2, 7, 1, 8]
        client.sort_data(data)
        self.assertEqual(data, [1, 2, 5, 7, 8])

if __name__ == '__main__':
    unittest.main()