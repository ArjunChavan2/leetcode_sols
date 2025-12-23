class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = ""
        while columnNumber > 0:
            columnNumber -= 1
            ret += alphabet[columnNumber % 26]
            columnNumber //= 26

        return ret[::-1]

# This solution runs in O(log n) time complexity and uses O(log n) space complexity. Since column number is 
# being divided by 26 in each iteration, the number of iterations is proportional to the logarithm of the column number.
# The space complexity is also O(log n) because the length of the result string is proportional to the number of iterations.