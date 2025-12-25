from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0 for _ in range(n)]
        memo[0] = 1
        for i in range(n):
            if memo[i] == 0:
                continue
            
            for j in range(i + 1, min(i + 1 + nums[i], n)):
                if memo[j] == 0:
                    memo[j] = memo[i] + 1
                else:
                    memo[j] = min(memo[j], memo[i] + 1)
        
        return memo[-1] - 1

# This solution runs in O(n^2) time complexity where n is the length of the input list nums. This is because it uses
# a nested loop structure: the outer loop iterates through each index of the list, and for each index, the inner 
# loop iterates up to nums[i] times to update the minimum jumps needed to reach each index. The total number of 
# operations performed in the worst case can be approximated to O(n^2). The space complexity is O(n) because the 
# memoization list 'memo' stores the minimum number of jumps needed to reach each index in the input list, resulting in n 
# elements stored in the list.