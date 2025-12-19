class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        memo = [0 for _ in range(len(nums))]
        if nums[0] > 0:
            memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(0, memo[i - 1] + nums[i])
        
        m = max(memo)
        if 0 not in nums and m == 0:
            return max(nums)
        return m


# This solution runs in O(n) time and uses O(n) space. By continually updating the memo array with the maximum local
# sum at each index, we ensure that the global maximum sum is always the maximum value in the memo array. The space
# complexity is O(n) because we are using an additional array to store the local maximum sums.