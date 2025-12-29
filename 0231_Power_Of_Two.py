from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        i = log2(abs(n))
        return abs(int(i) - i) < 1e-9

# This solution runs in O(1) time complexity because the logarithm operation and the subsequent calculations
# are performed in constant time regardless of the input value. Therefore, the overall time complexity is O(1).
# The space complexity is also O(1) because it uses a fixed amount of extra space.