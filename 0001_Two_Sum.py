class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums:
                i2 = nums.index(target-nums[i])
                if i != i2:
                    return [i, i2]

# This solution has a time complexity of O(n^2) in the worst case
# because the 'in' operation and 'index' method both take O(n) time.
# However, it is a brute-force approach that works correctly for the problem.