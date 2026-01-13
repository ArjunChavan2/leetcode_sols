from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        stack = []
        nextGreater = {}
        for i in range(n2):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextGreater[nums2[stack[-1]]] = nums2[i]
                del stack[-1]

            stack.append(i)
            
        ret = []
        for i in nums1:
            if i in nextGreater:
                ret.append(nextGreater[i])
            else:
                ret.append(-1)

        return ret
    
# This solution runs in O(n + m) time and O(n) space complexity where n is the length of nums2 and m is the length of 
# nums1. This is because it processes each element in nums2 once to build the nextGreater mapping using a stack,
# and then processes each element in nums1 to construct the result list. The space complexity is O(n) due to the storage
# of the nextGreater mapping which can contain up to n entries in the worst case.