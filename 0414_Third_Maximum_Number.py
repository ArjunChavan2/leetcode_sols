from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minVal = -2**31 - 1
        maxes = [minVal, minVal, minVal]
        n = len(nums)
        for i in range(n):
            if maxes[0] < nums[i] < maxes[1]:
                maxes[0] = nums[i]
            
            elif maxes[1] < nums[i] < maxes[2]:
                maxes[0] = maxes[1]
                maxes[1] = nums[i]

            elif maxes[2] < nums[i]:
                maxes[0] = maxes[1]
                maxes[1] = maxes[2]
                maxes[2] = nums[i]
        
        if maxes[0] == minVal:
            return maxes[2]
        return maxes[0]
        
# This solution runs in O(n) time complexity where n is the length of the input list nums. This is because the for loop
# iterates through the list once, performing a constant amount of work for each element to update the top three maximum
# values. Therefore, the overall time complexity is O(n). The space complexity is O(1) because it uses a fixed amount of extra space 
# (the maxes list with three elements) regardless of the input size.