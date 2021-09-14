import unittest

def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    charge = b - sum(bill) // 2
    
    if charge != 0:
        return charge
    
    return "Bon Appetit"

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(5, bonAppetit([3, 10, 2, 9], 1, 12))
        
    def test_two(self):
        self.assertEqual("Bon Appetit", bonAppetit([3, 10, 2, 9], 1, 7))

if __name__ == '__main__':
    unittest.main()