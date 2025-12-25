from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if len(nums) <= 1:
            return True
        memo = [False for _ in range(n)]
        memo[0] = True
        for i in range(n):
            if memo[i] == False:
                continue
            for j in range(nums[i]):
                if i + j + 1 >= n:
                    break
                memo[i + j + 1] = True
            if memo[-1]:
                return True
        return memo[-1]
    
# This solution runs in O(n^2) time complexity where n is the length of the input list nums. This is because it uses
# a nested loop structure: the outer loop iterates through each index of the list, and for each index, the inner loop 
# iterates up to nums[i] times to mark reachable indices. The total number of operations performed in the worst case 
# can be approximated to O(n^2). The space complexity is O(n) because the memoization list 'memo' stores a boolean 
# value for each index in the input list, resulting in n elements stored in the list.