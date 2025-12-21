class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-2) + climb(n-1)
                return memo[n]
    
        return climb(n)

# The solution runs in O(n) time and uses O(n) space. The time complexity is O(n) because the function climb is 
# called n times, and the space complexity is O(n) because the memo dictionary stores n values.