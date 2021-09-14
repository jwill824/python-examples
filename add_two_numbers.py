import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ListNode):
            return NotImplemented
        return self.val == o.val and self.next == o.next

def addTwoNumbers(l1: ListNode, l2: ListNode, c=0):
    val = l1.val + l2.val + c
    c = val // 10
    ret = ListNode(val % 10)
    
    if (l1.next or l2.next or c != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = addTwoNumbers(l1.next, l2.next, c)
        
    return ret

class test(unittest.TestCase):
    def test_one(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        l3 = ListNode(7, ListNode(0, ListNode(8)))
        
        self.assertEqual(l3, addTwoNumbers(l1, l2))

if __name__ == '__main__':
    unittest.main()