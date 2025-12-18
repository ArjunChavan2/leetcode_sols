class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = len(nums) - 1
        while i > 0:
            print(i)
            if nums[i - 1] == nums[i]:
                del nums[i]
            i-= 1
        
        return len(nums)

# This solution has a time complexity of O(n), where n is the length of the input list nums.
# The algorithm iterates through the list once, checking for duplicates and removing them in place.
# Since each element is processed only once, the overall time complexity is linear with respect to the size of the input list.