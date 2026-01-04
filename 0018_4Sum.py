from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4 or (len(nums) == 4 and sum(nums) != target):
            return []
        if len(nums) == 4:
            return [nums]
        ret = {}

        nums.sort()

        n = len(nums)
        for idx1 in range(n - 3):
            for idx2 in range(idx1 + 1, n - 2):
                l, r = idx2 + 1, n - 1
                print(idx1, idx2, l, r)
                while l < r:
                    s = nums[idx1] + nums[idx2] + nums[l] + nums[r]
                    
                    if s == target:
                        ret[nums[idx1], nums[idx2], nums[l], nums[r]] = 0
                        l += 1
                        r -= 1

                    elif s < target:
                        l += 1
                    
                    else:
                        r -= 1
        
        return list(ret.keys()) 

# This solution runs in O(n^3) time and O(n^2) space complexity where n is the length of the input list nums. This is because
# the solution uses three nested loops to iterate through the list. The two for loops each run in O(n) time and the while loop
# uses the two-pointer method which also runs in O(n) time. Since the loops are nested, the overall time complexity is O(n^3).
# The space complexity is O(n^2) in the worst case, where all quadruplets found are unique and stored in the ret dictionary.