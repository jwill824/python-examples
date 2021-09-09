import unittest

# We define a magic square to be an n x n matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

# You will be given a 3 x 3 matrix s of integers in the inclusive range [1,9]. We can convert any digit a to any other digit b in the range [1,9] at cost of |a - b|. Given s, convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].

def findTotalCostOfReplacement(s, ms):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if s[i][j] != ms[i][j]:
                count += abs(s[i][j] - ms[i][j])
    return count

def formingMagicSquare(s):
    ms = [
            [ [ 8, 1, 6 ], [ 3, 5, 7 ], [ 4, 9, 2 ] ],
            [ [ 6, 1, 8 ], [ 7, 5, 3 ], [ 2, 9, 4 ] ],
            [ [ 4, 9, 2 ], [ 3, 5, 7 ], [ 8, 1, 6 ] ],
            [ [ 2, 9, 4 ], [ 7, 5, 3 ], [ 6, 1, 8 ] ],
            [ [ 8, 3, 4 ], [ 1, 5, 9 ], [ 6, 7, 2 ] ],
            [ [ 4, 3, 8 ], [ 9, 5, 1 ], [ 2, 7, 6 ] ],
            [ [ 6, 7, 2 ], [ 1, 5, 9 ], [ 8, 3, 4 ] ],
            [ [ 2, 7, 6 ], [ 9, 5, 1 ], [ 4, 3, 8 ] ],
        ]
 
    _min = 30
    for i in range(0, 8):
        x = findTotalCostOfReplacement(s, ms[i])
        if x < _min:
            _min = x
     
    return _min
        
class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
  
    def test_two(self):
        self.assertEqual(4, formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
        
    def test_three(self):
        self.assertEqual(14, formingMagicSquare([[4, 5, 8], [2, 4, 1], [1, 9, 7]]))
        
    def test_four(self):
        self.assertEqual(30, formingMagicSquare([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
        
    def test_five(self):
        self.assertEqual(29, formingMagicSquare([[2, 2, 2], [2, 2, 2], [2, 2, 2]]))
        
if __name__ == '__main__':
    unittest.main()