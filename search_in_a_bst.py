import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, TreeNode):
            return NotImplemented
        return self.val == o.val and self.left == o.left and self.right == o.right
        
class Tree:        
    def __init__(self, root: TreeNode=None):
        self.root = root
    
    def search(self, val: int):
        curr = self.root
        
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        
        return None

class test(unittest.TestCase):
    def test_one(self):
        tree = Tree(TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(7, None, None)))
        self.assertEqual(TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), tree.search(2))
        
    def test_two(self):
        tree = Tree(TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(7, None, None)))
        self.assertEqual(None, tree.search(5))

if __name__ == '__main__':
    unittest.main()