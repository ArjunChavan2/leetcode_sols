# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        histA = []
        tempA = headA
        while tempA != None:
            histA.append(tempA)
            tempA = tempA.next
        
        histB = []
        while headB != None:
            histB.append(headB)
            headB = headB.next

        histA = histA[::-1]
        histB = histB[::-1]
        intersection = 0
        for i in range(len(histA)):
            if i == len(histB) or histA[i] != histB[i]:
                intersection = len(histA) - i
                break
            else:
                print(histA[i].val, histB[i].val)
            
        print(intersection)
        for i in range(intersection):
            headA = headA.next
        
        return headA

# This solution runs in O(n + m) time. By creating a list of both linked lists, we can iterate backwards to find the point
# where the two lists split. Then, after finding that, the solution iterates forward through list A and returns the node
# where they intersect.