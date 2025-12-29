class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ct = 1

        while n > ct:
            ct = 3 * ct

        return ct == n

# This solution runs in O(log n) time complexity where n is the input number. This is because the while loop
# multiplies ct by 3 until it is greater than or equal to n, which takes logarithmic time. The space complexity is O(1)
# because it uses a fixed amount of extra space regardless of the input size.