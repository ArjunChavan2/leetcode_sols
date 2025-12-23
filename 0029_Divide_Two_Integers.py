from math import log2

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        sign = 1
        if dividend < 0 and divisor > 0 or divisor < 0 and dividend > 0:
            sign = -1
        
        ret = int(2**(log2(abs(dividend)) - log2(abs(divisor)))) * sign

        if ret >= 2**31 - 1:
            return 2**31
        elif ret <= -2**31:
            return -2**31
        return ret

# This solution runs in O(1) time complexity and uses O(1) space complexity. Using the fact that the difference between 
# the logarithm of two numbers is equal to the logarithm of their ratio, this problem uses this to find the quotient.
# The quotient is then raised to the power of two to get rid of the log applied and then multiplied by the sign of the 
# dividend and divisor to get the final result.