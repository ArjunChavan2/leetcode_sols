from typing import List
import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        fact = math.factorial(rowIndex)
        for i in range(0, rowIndex+1):
            ret.append(fact // (math.factorial(rowIndex - i)*math.factorial(i)))
        return ret

# This solution runs in O(rowIndex) time complexity because it computes each element of the specific row.
# The loop iterates rowIndex + 1 times to calculate each element using the binomial coefficient formula.
# The factorial calculations are done using Python's built-in math.factorial function, which is efficient.
# The space complexity is also O(rowIndex) because the output list 'ret' contains rowIndex + 1 elements.