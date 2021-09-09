import unittest

# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# Example
# a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
# There are two subarrays meeting the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has 5 elements.

# Function Description
# Complete the pickingNumbers function in the editor below.

# pickingNumbers has the following parameter(s):
# int a[n]: an array of integers

# Returns
# int: the length of the longest subarray that meets the criterion

# Input Format
# The first line contains a single integer n, the size of the array a.
# The second line contains n space-separated integers, each an a[i].

# Constraints
# 2 <= n <= 100
# 0 <= a[i] < 100
# The answer will be >= 2.

def pickingNumbers(a):
    a.sort()
    subarray_len = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if (abs(a[i] - a[j])) <= 1:
                subarray_len = max(subarray_len, j - i + 1)
    return subarray_len

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(3, pickingNumbers([4, 6, 5, 3, 3, 1]))
        
    def test_two(self):
        self.assertEqual(5, pickingNumbers([1, 2, 2, 3, 1, 2]))

if __name__ == '__main__':
    unittest.main()