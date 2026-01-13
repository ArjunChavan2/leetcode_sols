from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        index = 1 # index starts at 1
        while index < left and curr is not None:
            prev = curr
            curr = curr.next
            index += 1
        
        stitch = prev
        stitchTail = curr
        prev = None
        
        while index <= right and curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            index += 1
        
        if stitch:
            stitch.next = prev
        else:
            head = prev
        
        stitchTail.next = curr
        
        return head

# This solution runs in O(n) time and O(1) space complexity where n is the length of the linked list. This is because
# it makes a single pass through the linked list, first to reach the left position, then continuing to reverse the 
# sublist between left and right, and finally reconnecting the reversed sublist back to the original list. The space
# complexity is O(1) since it uses only a constant amount of extra space for the pointers, regardless of the input size.