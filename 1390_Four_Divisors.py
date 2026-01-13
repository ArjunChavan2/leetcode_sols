from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        tot = 0
        def findDivisors(num):
            if num < 6:
                return 0
            ret = set()
            left = 1
            right = num
            while left <= right:
                if left * right == num:
                    ret.add(left)
                    ret.add(right)
                left += 1
                right = num // left

            if len(ret) == 4:
                return sum(ret)
            return 0

        for i in nums:
            tot += findDivisors(i)
        
        return tot

# This solution runs in O(n * sqrt(m)) time complexity where n is the length of the input list nums and m is the maximum
# value in nums. This is because for each number in nums, the findDivisors function iterates up to the square root of that
# number to find its divisors. In the worst case, this results in a time complexity of O(sqrt(m)) for each of the n numbers,
# leading to an overall time complexity of O(n * sqrt(m)).