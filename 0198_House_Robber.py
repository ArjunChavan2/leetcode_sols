from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        memo = nums[0:2]

        n = len(nums)
        for i in range(2, n):
            memo.append(max(memo[i - 1], memo[i - 2] + nums[i], memo[i - 1] - nums[i - 1] + nums[i]))
        
        return memo[-1]

# This solution runs in O(n) time and space complexity where n is the length of the input list nums. This is because it
# iterates through the list once, and for each element, performs a constant amount of work to update the memoization list 'memo'. 
# The space complexity is also O(n) because it is the same size as the input list, storing the maximum amount of money that can be 
# robbed up to each house. The memo stores the intermediate maximum between robbing the house before it, robbing the current house
# plus the maximum from two houses before, or adjusting for the case where the previous house was robbed but the current one is more profitable.