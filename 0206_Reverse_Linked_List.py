from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            print(curr.val)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

# This solution runs in O(n) time and O(1) space complexity where n is the length of the linked list. This is because
# it iterates through the linked list once, reversing the pointers in place.