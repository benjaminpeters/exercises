import random
import unittest
from binary_search import *

def generate_random_data(n):
    """Return a sorted list of n ints. """
    i = 0
    L = [random.randrange(1, n) for i in range(n)]
    return sorted(L)
    
class testingBinarySearch(unittest.TestCase):
    
    def test_empty(self):
        """Works on an empty list"""
        arr = []
        self.assertEqual(binarySearch(arr, 100), -1, "Should return -1")
        
    def test_one_item_not_found(self):
        """Works on 1 item list not containing searched object"""
        arr = [5]
        self.assertEqual(binarySearch(arr, 8), -1, "Should return -1")
    
    def test_one_item_found(self):
        """Works on 1 item list containing searched object"""
        arr = [10]
        self.assertEqual(binarySearch(arr, 10), 0, "Should return 0")
        
    def test_many_items_not_found(self):
        """Works on many item list not containing searched object"""
        arr = [1, 3, 6, 8, 10]
        self.assertEqual(binarySearch(arr, 9), -1, "Should return -1")
    
    def test_many_items_found(self):
        """Works on many item list containng searched object"""
        arr = [1, 3, 5, 8, 10, 13, 25]
        self.assertEqual(binarySearch(arr, 13), 5, "Should return 5")
        
    def test_uses_divide_and_conquer(self):
        """Works using a divide and conquer algorithm"""
        lookups = {}
        listLength = 10000
        proxyList = generate_random_data(listLength)
        smartList = []
        

if __name__ == '__main__':
    unittest.main(exit = False)