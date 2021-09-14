import unittest

def twoSum(nums, target):
    d = {}
    l = []
    for i in range(len(nums)):
        if target - nums[i] in d:
            l.append(d[target - nums[i]])
            l.append(i)
            break
        d[nums[i]] = i
    return l
            
class test(unittest.TestCase):
    def test_one(self):
        self.assertEqual([1, 2], twoSum([3, 2, 4], 6))

if __name__ == '__main__':
    unittest.main()