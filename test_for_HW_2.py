import unittest
import operator
from HW_2 import _min, _max, _sum, _mult
from functools import reduce

class Test_of_functions(unittest.TestCase):
    
    def test_of_min(self):
        self.assertEqual(_min(data), min(data))

    def test_of_max(self):
        self.assertEqual(_max(data), max(data))

    def test_of_sum(self):
        self.assertEqual(_sum(data), sum(data))

    def test_of_mult(self):
        self.assertEqual(_mult(data), reduce(operator.mul, data, 1))

if __name__ == '__main__':
    file_for_test = open('text_files/nums_5.txt', 'r')
    data = [int(x) for x in file_for_test.readline().split()]
    file_for_test.close()
    unittest.main()
