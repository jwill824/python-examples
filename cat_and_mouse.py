import unittest

def catAndMouse(x, y, z):
    if abs(x - z) < abs(y -z):
        return "Cat A"
    
    if abs(y - z) < abs(x -z):
        return "Cat B"
    
    if abs(x - z) == abs(y - z):
        return "Mouse C"

class test(unittest.TestCase):
    def test_one(self):
        q = int("2")
        
        _input = ["1 2 3", "1 3 2"]
        _expected = "Cat B\nMouse C"

        for q_itr in range(q):
            xyz = _input[q_itr].split()

            x = int(xyz[0])

            y = int(xyz[1])

            z = int(xyz[2])

            self.assertEqual(_expected.split("\n")[q_itr], catAndMouse(x, y, z))
        
if __name__ == '__main__':
    unittest.main()