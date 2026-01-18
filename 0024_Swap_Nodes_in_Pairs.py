from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = None
        first = head
        second = first.next

        while first != None and second != None:
            first.next = second.next
            second.next = first
            if prev is None:
                head = second
            else:
                prev.next = second
            
            prev = first
            first = first.next
            if first is None:
                break
            second = first.next
        
        return head

# This solution runs in O(n) time and O(1) space complexity where n is the length of the linked list. This is because
# the algorithm iterates through the linked list once, swapping pairs of nodes in place. This result in 0 additional
# space being used. 