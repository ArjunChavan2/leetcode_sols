from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        ret = 0
        diffs = {}

        for i, n in enumerate(nums):
            if n == 1:
                one += 1
            else:
                zero += 1
            
            if one - zero not in diffs:
                diffs[one - zero] = i
            

            if one == zero:
                ret = one + zero
            
            else:
                idx = diffs[one - zero]
                ret = max(ret, i - idx)
            
        
        return ret

# This solution runs in O(n) space and time complexity where n is the length of the input list nums. This is because
# it iterates through the list once, performing a constant amount of work for each element to update the counts of 
# zero and one, and to check and update the diffs dictionary. The space complexity is also O(n) in the worst case,
# where all the differences between the counts of ones and zeros are unique and therefore added to the dictionary.