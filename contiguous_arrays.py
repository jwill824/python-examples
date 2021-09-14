from typing import List
import unittest

"""
We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history

"""

def lcp(s, t):
    n = min(len(s),len(t))
    
    for i in range(n):
        if s[i] != t[i]:
            return s[0:i]
        
    return s[0:n]

def findContiguousHistory2(x: List, y: List):
    lrs = []
    z = x + y
    n = len(z)
    
    for i in range(n):
        for j in range(i + 1, n):
            w = lcp(z[i:n], z[j:n])
            
            if len(w) > len(lrs):
                lrs = w
                
    return lrs

def findContiguousHistory1(x: List, y: List):
    res = []
    
    n, m = len(x), len(y)
    i, j = 0, 0
    
    while i < n:
        while j < m:
            temp = []
            while i < n and j < m and x[i] == y[j]:
                temp.append(x[i])
                i += 1
                j += 1
            if len(temp) > len(res):
                res = temp
            j += 1
        i += 1
        j = 0
            
    return res

class test(unittest.TestCase):
    def test_one(self):
        user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
        user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
        self.assertEqual(["/pink", "/register", "/orange"], findContiguousHistory1(user0, user1))
        
    def test_two(self):
        user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
        user2 = ["a", "/one", "/two"]
        self.assertEqual([], findContiguousHistory1(user0, user2))
        
    def test_three(self):
        user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
        self.assertEqual(["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"], findContiguousHistory1(user0, user0))
        
    def test_four(self):
        user0 = list("abcde")
        user1 = list("acdef")
        self.assertEqual(["c", "d", "e"], findContiguousHistory1(user0, user1))

if __name__ == '__main__':
    unittest.main()