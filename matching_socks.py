import unittest

def sockMerchant(n, ar):
    matching_pairs = 0
    ar.sort(reverse = True)
    queue = ar
    prev_sock = queue.pop()
    while (queue != []):
        next_sock = queue.pop()
        if prev_sock < next_sock:
            prev_sock = queue.pop()
        if prev_sock == next_sock:
            matching_pairs += 1
            if queue != []:
                prev_sock = queue.pop()
    return matching_pairs

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(3, sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
        
    def test_two(self):
        self.assertEqual(9, sockMerchant(20, [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]))
        
    def test_three(self):
        self.assertEqual(30, sockMerchant(100, [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]))

if __name__ == '__main__':
    unittest.main()