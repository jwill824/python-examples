import unittest

def kangaroo(x1, v1, x2, v2):
    return 0

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual("YES", kangaroo([0, 3, 4, 2]))
        
    def test_two(self):
        self.assertEqual("NO", kangaroo([0, 2, 5, 3]))
        
if __name__ == '__main__':
    unittest.main()