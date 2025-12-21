class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r = nums.count(0)
        w = nums.count(1)
        for i in range(0, r):
            nums[i] = 0
        for i in range(r, r+w):
            nums[i] = 1
        for i in range(r+w,len(nums)):
            nums[i] = 2

# The solution runs in O(n) time and uses O(1) space. This is because the solution only uses a fixed amount
# of space to store the counts of the three colors, and it only iterates through the list once to set the values.