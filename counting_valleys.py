import unittest

def countingValleys(steps, path):
    sealevel = 0
    
    valley_exists = False
    valley_count = 0
    
    for i in range(steps):
        print(f'path = {path[i]}')
        
        if path[i] == 'U':
            sealevel += 1
            print(f'sealevel = {sealevel}')
        
        if path[i] == 'D':
            sealevel -= 1
            print(f'sealevel = {sealevel}')
            if sealevel < 0:
                valley_exists = True
                print(f'valley_exists = {valley_exists}')
                
        if sealevel == 0 and valley_exists:
            valley_exists = False
            valley_count += 1
            print(f'valley_count = {valley_count}')
            
    return valley_count

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, countingValleys(8, "UDDDUDUU"))
    
    def test_two(self):
        self.assertEqual(2, countingValleys(10, "DUDDDUUDUU"))
        
if __name__ == '__main__':
    unittest.main()