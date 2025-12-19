# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: list[ListNode]) -> bool:
        for i in range(10**4 + 1):
            if head == None:
                return False
            head = head.next
        return True








# The simplest solution is creating a vector of address and if the next node's address
# points to an address already in the vector, then there is a loop. This solution takes
# O(n) memory and time. A solution that takes O(1) memory and time is iterating through 
# the list 10^4 + 1 times and if by the end of loop, the node still points to a node, then 
# there is a cycle somewhere in the list.