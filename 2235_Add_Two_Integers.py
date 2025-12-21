import math

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if num1  == 0:
            return num2
        if num2 == 0:
            return num1

        return int(math.log2(2**num1 * 2**num2))

# This solution runs O(1) time and space. It uses the the property that when two exponents with the same base
# are multiplied, their exponents are added together. By taking the log of the result, we can get rid of the base
# and are left with the sum of the exponents without using the "+" or "-"operator.