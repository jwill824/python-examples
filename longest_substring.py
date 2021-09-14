import unittest

def lengthOfLongestSubstring(s: str) -> int:
    last_idx = {}
    max_len = 0
    start_idx = 0
 
    for i in range(len(s)):
        if s[i] in last_idx:
            start_idx = max(start_idx, last_idx[s[i]] + 1)
        max_len = max(max_len, i - start_idx + 1)
        last_idx[s[i]] = i
 
    return max_len
    
    
class test(unittest.TestCase):
    def test_one(self):        
        self.assertEqual(3, lengthOfLongestSubstring("abcabcbb"))
        
    def test_two(self):        
        self.assertEqual(1, lengthOfLongestSubstring("bbbbbb"))
        
    def test_three(self):        
        self.assertEqual(3, lengthOfLongestSubstring("pwwkew"))
        
    def test_four(self):        
        self.assertEqual(0, lengthOfLongestSubstring(""))
    
    def test_five(self):        
        self.assertEqual(1, lengthOfLongestSubstring("a"))

if __name__ == '__main__':
    unittest.main()