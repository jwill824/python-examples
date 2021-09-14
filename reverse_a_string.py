import unittest

def reverseAString(s):
    res = ""
    stack = []
    
    for ch in s:
        stack.append(ch)
        
    while stack:
        res += stack.pop()
        
    return res

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual("?ffeJ ,yadot gniod uoy era woH", reverseAString("How are you doing today, Jeff?"))

if __name__ == '__main__':
    unittest.main()