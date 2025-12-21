class Solution:
    def sqrtSearch(self, lower: int, upper: int, x: int) -> int:
        mid = (lower + upper) // 2
        if lower > upper:
            return upper
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            return self.sqrtSearch(mid + 1, upper, x)
        else:
            return self.sqrtSearch(lower, mid - 1, x)

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        return self.sqrtSearch(1, x, x)

# This solution runs in O(log n) time since it uses a binary search algorithm. The space complexity is 
# O(log n) due to the recursive calls. The solution works by recursively searching for the square root of x
# within a given range. If the square of the middle value is equal to x, then the middle value is the square root.
# If the square of the middle value is less than x, then the search continues in the upper half of the range. 
# If the square of the middle value is greater than x, then the search continues in the lower half of the range.
# The search continues until the lower bound exceeds the upper bound, at which point the upper bound is returned as the
# square root of x.