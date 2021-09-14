import unittest

from collections import Counter

# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]

# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

# Function Description
# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock

# Returns
# int: the number of pairs

# Input Format
# The first line contains an integer n, the number of socks represented in ar.
# The second line contains n space-separated integers, ar[i], the colors of the socks in the pile.

# Constraints
# 1 <= n <= 100
# 1 <= ar[i] <= 100 where 0 <= i < n

def sockMerchant(ar):
    c = Counter(ar)
    s = 0
    for i in c:
        s += c[i] // 2
    return s

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(3, sockMerchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
        
    def test_two(self):
        self.assertEqual(9, sockMerchant([4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]))
        
    def test_three(self):
        self.assertEqual(30, sockMerchant([44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]))

if __name__ == '__main__':
    unittest.main()