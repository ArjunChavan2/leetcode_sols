# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = head
        while prev != None and prev.val == val:
            prev = prev.next
        
        if prev == None:
            return None
        head = prev
        n = prev.next
        while n != None:
            if n.val == val:
                prev.next = n.next
            else:
                prev = n

            n = n.next

        return head

# The runtime is O(n) and the space complexity is O(1). The pointer prev is used to keep track of the 
# previous node in the list, and the pointer n is used to iterate through the list. The while 
# loop continues until n becomes None, which means the end of the list has been reached. If the current
# node's value is equal to val, the prev.next pointer is updated to skip the current node. Otherwise, 
# the prev pointer is updated to the current node. Finally, the head of the modified list is returned.