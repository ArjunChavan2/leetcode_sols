from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 1
        while last >= 0 and nums[last] == 0:
            last -= 1
        
        i = 0
        while i <= last:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                last -= 1
            else:
                i += 1

# This solution runs in O(n^2) time complexity because every time there is a zero in the list, the del operation
# takes O(n) time to shift the element and in the worst case, we may have to do this for all n elements.
# The space complexity is O(1) since we are modifying the list in place and not using any additional data structures.