from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = set()

        for i in range(10**4 + 1):
            if head == None:
                return None
            if head in d:
                return head
            d.add(head)
            head = head.next
        
        return None
        
# This solution runs in O(n) time and space complexity where n is the number of nodes in the linked list. This is because
# in the worst case, the head iterator will traverse all n nodes of the linked list, and each node address is stored in
# the hashtable 'd'. This creates a linear relationship between the number of nodes and both time and space used.