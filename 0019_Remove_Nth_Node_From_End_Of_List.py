from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        removedNode = -1
        i = head

        while removedNode < n and i != None:
            removedNode += 1
            i = i.next
        
        if i == None and removedNode < n - 1:
            return None
        
        if i == None and removedNode == n - 1:
            head = head.next
            return head


        removedNode = head
        while i != None:
            i = i.next
            removedNode = removedNode.next
        
        removedNode.next = removedNode.next.next

        return head

# This solution runs in O(L) time and O(1) space complexity where L is the length of the linked list. This is because
# it makes a single pass through the linked list with two pointers, first building and then maintaining a gap of n nodes
# between them. When the first pointer reaches the end of the list, the second pointer will be at the node just before the 
# one to be removed. The space complexity is O(1) because only a constant amount of extra space is used for the pointers,
# regardless of the input size.