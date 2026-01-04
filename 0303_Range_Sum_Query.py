from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.pSum = [nums[0]]
        for i in range(1, len(nums)):
            self.pSum.append(self.pSum[-1] + nums[i])
        print(self.pSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pSum[right]
        return self.pSum[right] - self.pSum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# This solution runs in O(n) time and space complexity for the constructor where n is the length of the input list nums.
# This is because it iterates through the list once to create the prefix sum array pSum, which takes O(n) time and space.
# The sumRange method runs in O(1) time complexity because it performs a constant amount of work to calculate the sum of the specified range
# using the prefix sum array. The space complexity for sumRange is O(1) as it does not use any additional space that scales with the input size.