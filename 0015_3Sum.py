from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = {}

        n = len(nums)
        for idx in range(n - 2):
            l = idx + 1
            r = n - 1
            while l < r:
                if nums[idx] + nums[l] + nums[r] == 0:
                    ret[nums[idx], nums[l], nums[r]] = 0
                    l += 1
                    r -= 1
                elif nums[idx] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return list(ret.keys())

# This solution runs in O(n^2) time and O(n) space complexity where n is the length of the input list nums. This is because
# the outer loop iterates through each element of the sorted list, and for each element, the inner while loop uses
# the two-pointer method to find pairs that sum to the negative of the current element. The two-pointer approach takes O(n) 
# time in the worst case, resulting in an overall time complexity of O(n^2). The space complexity is O(n) in the worst case,
# where all triplets found are unique and stored in the ret dictionary.