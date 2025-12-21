class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        if sum(nums) < abs(target):
            return 0

        rem = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums) - 1, -1, -1):
            rem[i] = rem[i + 1] + nums[i] # Uses DP to calc the amt remaining

        def backtrack(index, currentTot):
            if index == len(nums):
                return 1 if currentTot == target else 0
            
            if currentTot + rem[index] < target or currentTot - rem[index] > target: # Prunes branches too far away from target
                return 0
            
            a = backtrack(index + 1, currentTot + nums[index])
            b = backtrack(index + 1, currentTot - nums[index])
            return a + b

        return backtrack(0, 0)

# This solution runs in O(2^n) time complexity. Using backtracking, it calculates every permutation of nums and if the
# end sum is the target value, it returns 1 to indicate every unique way to reach the target. Additionally, if during
# the recursion the sum of the remaining numbers in nums is too small to reach the target from the current total, then
# the branch is pruned since there cannot be any permutations from there.