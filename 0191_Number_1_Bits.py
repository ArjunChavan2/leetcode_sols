class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(31, -1, -1):
            if n >= 2**i:
                n -= 2**i
                ret += 1
        
        return ret

# This solution runs in O(1) time complexity because the number of bits in a 32-bit integer is fixed, and the loop
# iterates a constant number of times (32 iterations) regardless of the input value. Therefore
# the overall time complexity is O(1). The space complexity is also O(1) because it uses a fixed amount of extra space
# (the variable 'ret' and the loop variable 'i') regardless of the input size.