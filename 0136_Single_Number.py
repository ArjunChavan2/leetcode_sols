from typing import List 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = nums[0]
        for i in nums[1:]:
            a = a ^ i
        return a

# This solution runs in O(n) time complexity where n is the length of the input list nums. This is because it iterates
# through the list once, performing a constant time XOR operation for each element. Therefore, the overall time complexity is O(n).
# The space complexity is O(1) because it uses a fixed amount of extra space (the variable 'a') regardless of the input size.