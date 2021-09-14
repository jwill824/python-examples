import unittest

def isBalanced(s):
    left_brackets = "([{"
    right_brackets = ")]}"
    
    stack = []
    
    for ch in s:
        if ch in left_brackets:
            stack.append(ch)
        if ch in right_brackets:
            if not stack:
                return "NO"
            top = stack.pop()
            if left_brackets.find(top) != right_brackets.find(ch):
                return "NO"
    
    return "YES" if not stack else "NO"
    
class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual("YES", isBalanced("{[()]}"))
        self.assertEqual("NO", isBalanced("{[(])}"))
        self.assertEqual("YES", isBalanced("{{[[(())]]}}"))
        
    def test_two(self):
        self.assertEqual("YES", isBalanced("{{([])}}"))
        self.assertEqual("NO", isBalanced("{{)[](}}"))
        
    def test_three(self):
        self.assertEqual("YES", isBalanced("{(([])[])[]}"))
        self.assertEqual("NO", isBalanced("{(([])[])[]]}"))
        self.assertEqual("YES", isBalanced("{(([])[])[]}[]"))

if __name__ == '__main__':
    unittest.main()