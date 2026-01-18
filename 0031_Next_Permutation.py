from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        incIter = n - 1
        while incIter > 0 and nums[incIter] <= nums[incIter - 1]:
            incIter -= 1
        
        if incIter == 0:
            nums.sort()
            return
        
        incIter -= 1
        swapIter = n - 1
        while swapIter > incIter and nums[swapIter] <= nums[incIter]:
            swapIter -= 1
        
        temp = nums[swapIter]
        nums[swapIter] = nums[incIter]
        nums[incIter] = temp

        nums[incIter + 1:] = sorted(nums[incIter+1::])

# This solution runs in O(n log n) time complexity where n is the length of the input list nums. This is because the algorithm
# performs two linear scans of the list to find the indices for swapping and then sorts the sublist after the swap index. The sorting step
# takes O(k log k) time where k is the length of the sublist, which in the worst case can be up to n, leading to an overall time complexity of 
# O(n log n). The space complexity is O(1) since the algorithm modifies the list in place and uses only a constant amount of extra space for variables.