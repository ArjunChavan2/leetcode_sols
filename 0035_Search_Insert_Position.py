class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index = 0
        while index < len(nums) and nums[index] < target:
            index+=1
        return index

# 2 + 1

# This solution runs in O(n) time complexity, where n is the length of the input list `nums`. It iterates through 
# the list from the beginning to the end, incrementing the `index` variable until it finds an element that is greater 
# than or equal to the target value. The function then returns the value of `index`, which represents the position 
# where the target value should be inserted to maintain the sorted order of the list.