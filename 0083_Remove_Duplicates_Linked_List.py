# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        t = head
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return t


# The solution runs in O(n) time complexity and uses O(1) space complexity. It iterates through the linked 
# list and removes any duplicate nodes by updating the next pointer of the current node to skip the next 
# node if it has the same value as the current node. The function returns the head of the modified linked list.