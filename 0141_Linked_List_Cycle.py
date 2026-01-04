# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: list[ListNode]) -> bool:
        if head == None:
            return False
        first = head
        second = head.next
        
        while second != None and second.next != None and first != second:
            first = first.next
            second = second.next.next
        
        return first == second








# This solution runs in O(n) time and O(1) space complexity where n is the number of nodes in the linked list. This is
# because in the worst case, the first pointer will traverse all n nodes of the linked list, while the second pointer
# moves at twice the speed. If there is a cycle, the two pointers will eventually meet; if not, the second pointer will 
# reach the end of the list. The space complexity is O(1) because only a constant amount of extra space is used for the two pointers,
# regardless of the input size.