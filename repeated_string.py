import unittest

def repeatedString(s: str, n):
    floor = n // len(s)
    leftover = s[:(n % len(s))]
    return s.count('a') * floor + leftover.count('a')

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(7, repeatedString("aba", 10))
        
    def test_two(self):
        self.assertEqual(1000000000000, repeatedString("a", 1000000000000))
        
    def test_three(self):
        self.assertEqual(588525, repeatedString("aab", 882787))
        
    def test_four(self):
        self.assertEqual(0, repeatedString("x", 970770))
        
    def test_five(self):
        self.assertEqual(51574523448, repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm", 736778906400))
        
if __name__ == '__main__':
    unittest.main()