from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        return (l * (l + 1) // 2) - sum(nums)

# This solution runs in O(n) time complexity where n is the length of the input list nums. This is because it iterates
# through the list once to calculate the sum of its elements, which takes O(n) time. The calculation of the expected sum 
# using the Euler's formula takes constant time O(1). Therefore, the overall time complexity is O(n). The space complexity 
# is O(1) because it uses a fixed amount of extra space.