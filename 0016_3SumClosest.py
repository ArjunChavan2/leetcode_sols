from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ret = 10e4 + 1
        n = len(nums)
        for idx in range(n - 2):
            l = idx + 1
            r = n - 1

            while l < r:
                curr = nums[idx] + nums[l] + nums[r]
                if abs(target - curr) < abs(target - ret):
                    ret = curr
                
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    return curr
        
        return ret

# This solution runs in O(n^2) time and O(1) space complexity where n is the length of the input list nums. This is 
# because the outer loop iterates through each element of the sorted list, and for each element, the inner while loop 
# uses the two-pointer method to find the closest sum to the target. The two-pointer approach takes O(n) time in the 
# worst case, resulting in an overall time complexity of O(n^2). The space complexity is O(1) as it uses a constant
# amount of extra space regardless of the input size.