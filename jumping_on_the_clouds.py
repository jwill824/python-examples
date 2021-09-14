import unittest

def jumpingOnClouds(clouds):
    jumps = 0
    i = 0
    
    while i < len(clouds) - 1:
        if clouds[i] == 0:
            i += 1
        jumps += 1
        i += 1
    
    return jumps
    
class test(unittest.TestCase):
    def test_one(self):        
        self.assertEqual(4, jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
        
    def test_two(self):        
        self.assertEqual(3, jumpingOnClouds([0, 0, 0, 1, 0, 0]))

if __name__ == '__main__':
    unittest.main()