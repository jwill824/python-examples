import unittest

import re

def reverseASentence(s):
    stack = []
    sentence = re.findall("[\w]+|[?.,!]", s)
    new_sentence = []
    res = ""
    punctuations = []
    
    for i, word in enumerate(sentence):
        if word not in "?.,!":
            stack.append(word)
        else:
            punctuations.append((i, word))
        
    while stack:
        new_sentence.append(stack.pop())
        
    for punctuation in punctuations:
        new_sentence.insert(punctuation[0], punctuation[1])
        
    first_word = True
    for i, word in enumerate(new_sentence):
        if first_word or word in "?.,!":
            res += word
            first_word = False
        else:
            res += " " + word
        
    return res

class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual("Jeff today doing you are, How?", reverseASentence("How are you doing today, Jeff?"))

if __name__ == '__main__':
    unittest.main()