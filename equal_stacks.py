from typing import List
import unittest

def equalStacks(h1: List, h2: List, h3: List):
    s1, s2, s3 = map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        m = min(s1, s2, s3)
        while s1 > m: 
            s1 -= h1.pop(0)
        while s2 > m: 
            s2 -= h2.pop(0)
        while s3 > m: 
            s3 -= h3.pop(0)
        if s1 == s2 == s3: 
            return s1
    return 0

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(5, equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]))

    def test_two(self):
        self.assertEqual(5, equalStacks([1, 1, 1, 1, 1], [3, 2], [1, 3, 1]))

if __name__ == '__main__':
    unittest.main()