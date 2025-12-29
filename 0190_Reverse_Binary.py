class Solution:
    def reverseBits(self, n: int) -> int:
        string = str(bin(n))[2:][::-1]
        return int(string+(32 - len(string))*'0',2)

# This solution runs in O(1) time complexity because the number of bits in a 32-bit integer is fixed, and the operations
# performed (conversion to binary string, reversing the string, padding with zeros, and converting back to an integer) all take constant time regardless of the input value. 
# The space complexity is also O(1) because the amount of extra space used does not depend on the size of the input; it only requires a fixed amount of space for the string representation of the bits.